import json
from typing import List, Dict, Any
from colorama import Fore, Style

def format_findings(findings: List[Dict[str, Any]], as_json: bool = False) -> None:
    if as_json:
        print(json.dumps(findings, indent=2))
        return

    if not findings:
        print(f"\n{Fore.GREEN}[+] No vulnerabilities found! Happy coding.{Style.RESET_ALL}")
        return

    print(f"\n{Fore.YELLOW}[!] Scanning complete. Found {len(findings)} issues:{Style.RESET_ALL}\n")

    for issue in findings:
        severity = issue.get('severity', 'LOW')
        color = Fore.BLUE
        
        if severity == 'HIGH':
            color = Fore.RED
        elif severity == 'MEDIUM':
            color = Fore.YELLOW

        print(f"{color}[{severity}] {issue['category']}{Style.RESET_ALL}")
        print(f"{Style.DIM}Message: {issue['message']}{Style.RESET_ALL}")
        print(f"File: {issue['file']}:{issue['line']}")
        print(f"Code: {Fore.WHITE}{issue['code']}{Style.RESET_ALL}")
        print("-" * 40)

def print_summary(findings: List[Dict[str, Any]]) -> None:
    count = len(findings)
    if count == 0:
        return
        
    high = sum(1 for f in findings if f['severity'] == 'HIGH')
    med = sum(1 for f in findings if f['severity'] == 'MEDIUM')
    low = sum(1 for f in findings if f['severity'] == 'LOW')
    
    print(f"\n{Style.BRIGHT}Scan Summary:{Style.RESET_ALL}")
    print(f"  Total Issues: {count}")
    print(f"  {Fore.RED}High: {high}{Style.RESET_ALL}")
    print(f"  {Fore.YELLOW}Medium: {med}{Style.RESET_ALL}")
    print(f"  {Fore.BLUE}Low: {low}{Style.RESET_ALL}")

