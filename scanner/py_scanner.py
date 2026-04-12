from typing import List, Dict, Any

from scanner.rules.secrets import check_secrets
from scanner.rules.dangerous import check_dangerous
from scanner.rules.crypto import check_crypto

def scan_py_file(filepath: str) -> List[Dict[str, Any]]:
    findings: List[Dict[str, Any]] = []

    try:
        with open(filepath, "r", encoding="utf-8", errors="replace") as fh:
            for line_number, line in enumerate(fh, start=1):
                stripped = line.strip()
                if not stripped or stripped.startswith("#"):
                    continue

                findings.extend(check_secrets(line, line_number, filepath))
                findings.extend(check_dangerous(line, line_number, filepath, lang="python"))
                findings.extend(check_crypto(line, line_number, filepath))

    except (OSError, PermissionError) as exc:
        print(f"  [!] Cannot read {filepath}: {exc}")

    return findings

