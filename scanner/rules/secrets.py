import re
from typing import List, Dict, Any

# Patterns that indicate hardcoded secrets
SECRET_PATTERNS = [
    (re.compile(r'(?i)(api[_-]?key|apikey)\s*[=:]\s*["\']([A-Za-z0-9\-_\.]{8,})["\']'), 'Hardcoded API Key'),
    (re.compile(r'(?i)(secret[_-]?key|secret)\s*[=:]\s*["\']([A-Za-z0-9\-_\.!@#$%^&*]{8,})["\']'), 'Hardcoded Secret Key'),
    (re.compile(r'(?i)(password|passwd|pwd)\s*[=:]\s*["\']([^"\']{4,})["\']'), 'Hardcoded Password'),
    (re.compile(r'(?i)(token|auth[_-]?token|access[_-]?token)\s*[=:]\s*["\']([A-Za-z0-9\-_\.]{8,})["\']'), 'Hardcoded Token'),
    (re.compile(r'(?i)(stripe[_-]?key|sk-test-|sk-live-)([A-Za-z0-9]{10,})'), 'Hardcoded Stripe Key'),
    (re.compile(r'(?i)(aws[_-]?access[_-]?key|aws[_-]?secret)\s*[=:]\s*["\']([A-Za-z0-9+/]{20,})["\']'), 'Hardcoded AWS Credential'),
    (re.compile(r'(?i)(private[_-]?key)\s*[=:]\s*["\']([A-Za-z0-9\-_\.]{8,})["\']'), 'Hardcoded Private Key'),
    (re.compile(r'(?i)(db[_-]?password|database[_-]?password)\s*[=:]\s*["\']([^"\']{4,})["\']'), 'Hardcoded DB Password'),
]


def check_secrets(line: str, line_number: int, filepath: str) -> List[Dict[str, Any]]:
    findings: List[Dict[str, Any]] = []

    for pattern, label in SECRET_PATTERNS:
        if pattern.search(line):
            findings.append({
                "category": "Hardcoded Secret",
                "severity": "HIGH",
                "message": f"{label} detected — move to environment variables or a secrets manager.",
                "file": filepath,
                "line": line_number,
                "code": line.strip(),
            })
            break  # One finding per line to avoid duplicates

    return findings
