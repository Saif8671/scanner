# Industrial Vulnerability Scanner

An industrial-grade vulnerability scanner with multiple scanning capabilities including Web Application Scanners, Network Scanners, and Static Analysis tools. Built for comprehensive security assessment and risk evaluation.

## Features

### Core Scanning Modules
- **Web Application Scanners**: XSS, SQL Injection, Security Header checks
- **Network Scanners**: Port scanning, service detection, insecure protocol identification
- **Static Analysis**: Source code vulnerability detection

### Key Capabilities
- **Reconnaissance**: Domain/IP resolution, subdomain enumeration
- **Vulnerability Detection**: Automated security flaw identification
- **Risk Scoring**: Weighted vulnerability prioritization system
- **Report Generation**: JSON/HTML formatted reports with database storage

## Installation
### Prerequisites
``` bash
pip install requirements.txt
```
Run the Scanner
```bash
python vulnerability_scanner_app.py 
```
## Module Details
### Web Application Scanner
- Cross-Site Scripting (XSS) detection
- SQL Injection vulnerability identification
- Missing security header analysis
- Response-based vulnerability detection
### Network Scanner
- Comprehensive port scanning
- Service fingerprinting
- Insecure protocol detection
- Critical port exposure assessment
- Static Analysis Engine
- Hardcoded credential detection
- SQL query parameterization checks
- Cryptographic weakness identification
- Code quality assessment
### Risk Scoring System
- Critical: 20 points
- High: 10 points
- Medium: 5 points
- Low: 1 point
Maximum score: 100 points

## License
This project is licensed under the MIT License - see the source code for details.


## Disclaimer
This tool is intended for educational and authorized security testing purposes only. The developers are not responsible for any misuse or damage caused by this tool.