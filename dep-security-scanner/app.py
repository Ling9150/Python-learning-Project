import streamlit as st
from datetime import datetime

from parser.requirements_parser import parse_req
from cache import init_db,get_cache,save_cache
from scan import check,parse_vulns,get_ai_advice,generate_report

st.set_page_config(
    page_title="Dependency Security Scanner",
    layout="wide"
)

st.title("Dependency Security Scanner")

uploaded_file = st.file_uploader(
    "Upload requirements.txt",
    type = ["txt"]
)

ai_limit = st.number_input(
    "AI advice limit",
    min_value=0,
    max_value=10,
    value=0
)

if uploaded_file is not None:
    with open("uploaded_requirements.txt", "wb") as f:
        f.write(uploaded_file.getvalue())

    if st.button("Scan"):
        with st.spinner("Scanning dependencies..."):
            init_db()

            target_path = "uploaded_requirements.txt"
            deps = parse_req(target_path)

            all_vulns = []
            ai_advice_list = []

            total_vulns = 0
            critical_count = 0
            high_count = 0
            moderate_count = 0
            low_count = 0
            unknown_count = 0
            ai_used = 0
            for dep in deps:
                raw_result = get_cache(dep.name, dep.version)

                if raw_result is None:
                    raw_result = check(dep)
                    save_cache(
                        dep.name,
                        dep.version,
                        raw_result,
                        datetime.now().isoformat()
                    )

                clean_result = parse_vulns(raw_result, dep)

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

                    if ai_used < ai_limit:
                        advice = get_ai_advice(item)
                        ai_advice_list.append({
                            "package": item.pac_name,
                            "vulnerability_id": item.vuln_id,
                            "advice": advice
                        })
                        ai_used += 1

            st.subheader("Scan Summary")

            col1, col2, col3, col4, col5, col6 = st.columns(6)
            col1.metric("Dependencies", len(deps))
            col2.metric("Total", total_vulns)
            col3.metric("Critical", critical_count)
            col4.metric("High", high_count)
            col5.metric("Moderate", moderate_count)
            col6.metric("Unknown", unknown_count)

            rows = []
            for vuln in all_vulns:
                rows.append({
                    "Package": vuln.pac_name,
                    "Version": vuln.version,
                    "Severity": vuln.severity,
                    "Vulnerability ID": vuln.vuln_id,
                    "Summary": vuln.summary
                })

            st.subheader("Vulnerability Results")
            st.dataframe(rows, use_container_width=True)

            if ai_advice_list:
                st.subheader("AI Advice")
                for advice_item in ai_advice_list:
                    st.markdown(f"### {advice_item['package']} - {advice_item['vulnerability_id']}")
                    st.write(advice_item["advice"])

            stats = {
                "total": total_vulns,
                "critical": critical_count,
                "high": high_count,
                "moderate": moderate_count,
                "low": low_count,
                "unknown": unknown_count
            }

            generate_report(
                "streamlit_report.md",
                target_path,
                deps,
                all_vulns,
                stats
            )
            with open("streamlit_report.md", "r", encoding="utf-8") as f:
                report_text = f.read()

            st.download_button(
                label="Download Markdown Report",
                data=report_text,
                file_name="dependency_security_report.md",
                mime="text/markdown"
            )