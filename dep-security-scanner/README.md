# AI Dependency Security Scanner

An AI-assisted dependency security scanner for small teams. It reads a dependency file, queries the OSV vulnerability database, caches results locally, and generates readable risk explanations and repair suggestions.

## Features

- Parse Python dependency files
- Query OSV vulnerability database
- Cache vulnerability results with SQLite
- Show scan results in CLI with Rich tables
- Generate Markdown reports
- Provide AI-based remediation advice
- Provide a Streamlit web interface
- Support Docker and GitHub Actions integration

## Tech Stack

- Python
- requests
- sqlite3
- Rich
- Streamlit
- OSV API
- SiliconFlow / OpenAI-compatible API

## Installation

```bash
pip install -r requirements.txt
```

## Configure API Key
The AI advice feature reads the API key from an environment variable.
Windows PowerShell:
```powershell
$env:SILICONFLOW_API_KEY="your_api_key_here"
```
Windows CMD:
```bat
set SILICONFLOW_API_KEY=your_api_key_here
```
macOS / Linux:
```bash
export SILICONFLOW_API_KEY="your_api_key_here"
```

If the API key is not configured, the scanner will skip AI advice.
## CLI Usage

```bash
python scan.py -f test_files/sample_requirements.txt
```

Generate a custom report:
```bash
python scan.py -f test_files/sample_requirements.txt --output report.md
```

Disable AI advice during scanning:
```bash
python scan.py -f test_files/sample_requirements.txt --ai-limit 0
```

## Streamlit Usage
```bash
streamlit run app.py
```

Then upload a requirements file and click Scan.

## Docker Usage

Build the image:
```bash
docker build -t dep-security-scanner .
```

Run the Streamlit app:
```bash
docker run --rm -p 8501:8501 dep-security-scanner
```

Run CLI scan:
```bash
docker run --rm dep-security-scanner python scan.py -f test_files/sample_requirements.txt --ai-limit 0
```

## Report Output

The scanner generates a Markdown report containing:
- Scan file
- Scan time
- Number of dependencies scanned
- Vulnerability summary
- Vulnerability details
- Severity levels
- AI remediation advice when enabled

## Project Value

This project helps small teams discover dependency security risks before they become production issues. It combines structured vulnerability data from OSV with AI-generated explanations, making security results easier to understand and act on.