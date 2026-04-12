import re
from typing import List, Dict, Any

CRYPTO_PATTERNS = [
    (re.compile(r'\bmd5\b', re.IGNORECASE), 'MD5', 'MEDIUM',
     'MD5 is cryptographically broken — use SHA-256 or stronger.'),
    (re.compile(r'\bsha1\b', re.IGNORECASE), 'SHA-1', 'MEDIUM',
     'SHA-1 is weak and collision-prone — use SHA-256 or stronger.'),
    (re.compile(r'\bDES\b'), 'DES', 'HIGH',
     'DES encryption is insecure — use AES-256 instead.'),
    (re.compile(r'\bRC4\b', re.IGNORECASE), 'RC4', 'HIGH',
     'RC4 is a broken stream cipher — use AES-GCM or ChaCha20.'),
    (re.compile(r'createHash\(["\']md5["\']\)', re.IGNORECASE), 'MD5 (Node crypto)', 'MEDIUM',
     'MD5 hash via Node.js crypto is cryptographically broken — use SHA-256.'),
    (re.compile(r'createHash\(["\']sha1["\']\)', re.IGNORECASE), 'SHA-1 (Node crypto)', 'MEDIUM',
     'SHA-1 hash via Node.js crypto is weak — use SHA-256.'),
    (re.compile(r'hashlib\.(md5|sha1)\s*\(', re.IGNORECASE), 'Weak hashlib algorithm', 'MEDIUM',
     'MD5/SHA-1 via hashlib is cryptographically weak — use hashlib.sha256() or better.'),
]


def check_crypto(line: str, line_number: int, filepath: str) -> List[Dict[str, Any]]:
    findings: List[Dict[str, Any]] = []
    seen: set = set()

    for pattern, algorithm, severity, message in CRYPTO_PATTERNS:
        if pattern.search(line) and algorithm not in seen:
            seen.add(algorithm)
            findings.append({
                "category": "Weak Cryptography",
                "severity": severity,
                "message": f"{algorithm} detected — {message}",
                "file": filepath,
                "line": line_number,
                "code": line.strip(),
            })

    return findings

