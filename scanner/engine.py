from typing import List, Dict, Any
import os

from scanner.js_scanner import scan_js_file
from scanner.py_scanner import scan_py_file
from utils.file_loader import load_files

def run_scan(target_path: str) -> List[Dict[str, Any]]:
    all_findings = []
    
    files_to_scan = load_files(target_path)
    
    if not files_to_scan:
        return []

    for filepath in files_to_scan:
        if filepath.endswith('.js'):
            all_findings.extend(scan_js_file(filepath))
        elif filepath.endswith('.py'):
            all_findings.extend(scan_py_file(filepath))
            
    return all_findings
