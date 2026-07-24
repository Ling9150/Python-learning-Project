from datetime import datetime
import requests
from openai import OpenAI
from parser.requirements_parser import parse_req
from vulnerability import Vulnerability
from cache import init_db,save_cache,get_cache
import argparse
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
import os

def check(dep):
    url = "https://api.osv.dev/v1/query"
    payload = {
        "package":{
            "name":dep.name,
            "ecosystem":"PyPI"
        },
        "version":dep.version
    }
    try:
        res = requests.post(url,json=payload)
        res.raise_for_status()
        return res.json()
    except Exception as e:
        print(f"Error querying OSV API for {dep.name}:{e}")
        return {}  #return an empty

def parse_vulns(api_res,dep):
    vulns = api_res.get("vulns",None)
    if not vulns:
        return []  #"None" will cause an error
    clean_list = []
    for vuln in vulns:
        vuln_id = vuln.get("id","N")
        summary = vuln.get("summary","No Summary")
        db_spe = vuln.get("database_specific",{})
        severity = db_spe.get("severity","Unknown")
        item = Vulnerability(
            pac_name = dep.name,
            vuln_id = vuln_id,
            summary = summary,
            severity = severity,
            version = dep.version
        )
        clean_list.append(item)

        #clean_list.append("\n")   #no effect
    return clean_list

def parse_args():
    parser = argparse.ArgumentParser(
        description="AI dependency security scanner"
    )
    parser.add_argument(
        "--output",
        default="report.md",
        help="Path to save markdown report"
    )
    parser.add_argument(
        "-f",
        "--file",
        required=True,
        help="Path to requirements.txt"
    )
    parser.add_argument(
        "--ai-limit",
        type=int,
        default=1,
        help="Maximum number of vulnerabilities to analyze with AI"
    )
    return parser.parse_args()

def get_ai_advice(vuln):
    api_key = os.getenv("SILICONFLOW_API_KEY")
    if not api_key:
        return "AI advice skipped:SILICONFLOW_API_KEY is not set"
    client = OpenAI(
        api_key = api_key,
        base_url = "https://api-inference.modelscope.cn/v1/"
    )
    prompt = f"""
    you are a security engineer,please analyze the following vulnerability:
    Package name:{vuln.pac_name},
    Version:{vuln.version},
    Severity:{vuln.severity},
    Description:{vuln.summary}
    Please output:
    1.Vulnerability impact,
    2.Remediation recommendations,
    3.Upgrade command"""
    try:
        response = client.chat.completions.create(
            model = "deepseek-ai/DeepSeek-V4-Flash",
            messages = [
                {
                    "role":"user",
                    "content":prompt
                }
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"AI advice failed:{e}"

def generate_report(output_path,target_path,deps,all_vulns,stats):
    with open(output_path,"w",encoding="utf-8")as f:
        f.write("#Dependency Security Scan Report\n\n")

        f.write(f"Scan file: {target_path}\n\n")
        f.write(f"Scan time: {datetime.now().isoformat()}\n\n")
        f.write("## Summary\n\n")
        f.write(f"- Dependencies scanned: {len(deps)}\n")
        f.write(f"- Total vulnerabilities: {stats['total']}\n")
        f.write(f"- Critical: {stats['critical']}\n")
        f.write(f"- High: {stats['high']}\n")
        f.write(f"- Moderate: {stats['moderate']}\n")
        f.write(f"- Low: {stats['low']}\n")
        f.write(f"- Unknown: {stats['unknown']}\n\n")
        f.write("## Vulnerabilities\n\n")
        f.write("| Package | Version | Severity | Vulnerability ID | Summary |\n")
        f.write("|---|---|---|---|---|\n")
        for vuln in all_vulns:
            f.write(
                f"|{vuln.pac_name}|{vuln.version}|{vuln.severity}|{vuln.vuln_id}|{vuln.summary}|\n"
            )

def main():
    args = parse_args()
    console = Console()
    all_vulns = []
    init_db()
    target_path = args.file
    deps = parse_req(target_path)

    total_vulns = 0
    critical_count = 0
    high_count = 0
    moderate_count = 0
    low_count = 0
    unknown_count = 0
    ai_used = 0

    #print(deps)
    console.print(f"[green]Loaded {len(deps)} dependencies[/green]")

    for dep in deps:
        if dep.version is None:
            console.print(f"[yellow]Skipped {dep.name}: version is not specified[/yellow]")
            continue
        raw_result = get_cache(
            dep.name,
            dep.version
        )
        if raw_result is None:
            raw_result = check(dep)
            save_cache(
                dep.name,
                dep.version,
                raw_result,
                datetime.now().isoformat()
            )
        #print("API Response:")
        clean_result = parse_vulns(raw_result,dep)
#    test_dep = deps[0]
#    print(test_dep)
#    print(f"Checking vulnerability for {test_dep.name} v{test_dep.version} ...")
#    raw_result = check(test_dep)
#    print("API Response:")
#    clean_result = parse_vulns(raw_result)
        for item in clean_result:
            all_vulns.append(item)
            total_vulns += 1
            if item.severity == "CRITICAL":
                critical_count += 1
            elif item.severity == "HIGH":
                high_count += 1
            elif item.severity == "MODERATE":
                moderate_count += 1
            elif item.severity == "LOW":
                low_count += 1
            else:
                unknown_count += 1
            #print(item)
            if ai_used < args.ai_limit:
                advice = get_ai_advice(item)
                print(advice)
                ai_used += 1
        print("\n")

    table = Table(title="Vulnerability Results")
    table.add_column("Package",style="bright_black")
    table.add_column("Version",style="bright_black")
    table.add_column("Severity",style="bright_red")
    table.add_column("Vulnerability ID",style="bright_black")
    table.add_column("Summary",style="yellow")
    for vuln in all_vulns:
        table.add_row(
            vuln.pac_name,
            vuln.version,
            vuln.severity,
            vuln.vuln_id,
            vuln.summary
        )
    console.print(table)

    summary_text = f"""
    Dependencies scanned: {len(deps)}
    Total vulnerabilities: {total_vulns}
    Critical: {critical_count}
    High: {high_count}
    Moderate: {moderate_count}
    Low: {low_count}
    Unknown: {unknown_count}
    """

    stats = {
        "total": total_vulns,
        "critical": critical_count,
        "high": high_count,
        "moderate": moderate_count,
        "low": low_count,
        "unknown": unknown_count
    }
    generate_report(args.output,target_path,deps,all_vulns,stats)

    console.print(Panel(summary_text, title="Scan Summary", border_style="bright_cyan"))

#    print("Scan Summary")
#    print(f"Dependencies scanned: {len(deps)}")
#    print(f"Total vulnerabilities: {total_vulns}")
#    print(f"Critical: {critical_count}")
#    print(f"High: {high_count}")
#    print(f"Moderate: {moderate_count}")
#    print(f"Low: {low_count}")
#    print(f"Unknown: {unknown_count}")

if __name__ == "__main__":
    main()