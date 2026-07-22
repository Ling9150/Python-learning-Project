import requests
from openai import OpenAI
from parser.requirements_parser import parse_req
from vulnerability import Vulnerability

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

def get_ai_advice(name,version,vulns):
        client = OpenAI(
            api_key="sk-jtlpwtiqvfrxrqplbwvlludvfrjslegylubruwxflcrxhrps",
            base_url = "https://api.siliconflow.cn/v1"
        )


def main():
    target_path = "test_files/sample_requirements.txt"
    deps = parse_req(target_path)
    print(deps)
    print(f"Loaded {len(deps)} dependencies")
    for dep in deps:
        raw_result = check(dep)
        print("API Response:")
        clean_result = parse_vulns(raw_result,dep)
#    test_dep = deps[0]
#    print(test_dep)
#    print(f"Checking vulnerability for {test_dep.name} v{test_dep.version} ...")
#    raw_result = check(test_dep)
#    print("API Response:")
#    clean_result = parse_vulns(raw_result)
        for item in clean_result:
            print(item)
            print("\n")
if __name__ == "__main__":
    main()