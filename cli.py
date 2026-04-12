import argparse
import sys
import os

from banner import display_banner, __version__
from scanner.engine import run_scan
from report.formatter import format_findings, print_summary

def main():
    parser = argparse.ArgumentParser(
        description="VulnHawk - Static Application Security Testing (SAST) Scanner",
        add_help=True
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    scan_parser = subparsers.add_parser("scan", help="Scan a file or directory")
    scan_parser.add_argument("path", help="The path to scan (file or directory)")
    scan_parser.add_argument("--json", action="store_true", help="Output results in JSON format")
    
    parser.add_argument("-v", "--version", action="version", version=f"VulnHawk v{__version__}")

    if len(sys.argv) == 1:
        display_banner()
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()

    if args.command == "scan":
        display_banner()
        print(f"[*] Starting scan on: {args.path}...")
        
        try:
            findings = run_scan(args.path)
            format_findings(findings, as_json=args.json)
            
            if not args.json:
                print_summary(findings)
                
        except Exception as e:
            print(f"[ERROR] An unexpected error occurred: {e}")
            sys.exit(1)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
