# Save this as: run_scanner.py
from industrial_vulnerability_scanner import IndustrialVulnerabilityScanner

def main():
    # Initialize scanner
    scanner = IndustrialVulnerabilityScanner()
    
    # Set target (use a test target - don't scan systems without permission!)
    scanner.set_target("testphp.vulnweb.com")  # Test site provided for security testing
    
    # Perform all scanning phases
    print("Starting vulnerability scan...")
    scanner.reconnaissance()
    scanner.web_application_scan()
    scanner.network_scan()
    scanner.static_analysis()
    scanner.calculate_risk_scores()
    
    # Generate reports
    json_report = scanner.generate_report("json")
    html_report = scanner.generate_report("html")
    
    print(f"\n[+] Scan Complete!")
    print(f"[+] JSON Report: {json_report}")
    print(f"[+] HTML Report: {html_report}")
    print(f"[+] Overall Risk Score: {scanner.results['risk_scores']['overall']}/100")

if __name__ == "__main__":
    main()
