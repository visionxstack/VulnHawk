import re
from typing import List, Dict, Any

# Python dangerous functions
PYTHON_DANGEROUS = [
    (re.compile(r'\beval\s*\('), 'eval()', 'HIGH',
     'eval() executes arbitrary code — never pass untrusted input to it.'),
    (re.compile(r'\bexec\s*\('), 'exec()', 'HIGH',
     'exec() executes arbitrary code — avoid with user-supplied data.'),
    (re.compile(r'\bpickle\.loads?\s*\('), 'pickle.load()', 'HIGH',
     'pickle deserialization of untrusted data can lead to remote code execution.'),
    (re.compile(r'\bsubprocess\.(call|run|Popen)\s*\(.*shell\s*=\s*True'), 'subprocess shell=True', 'HIGH',
     'subprocess with shell=True is vulnerable to shell injection.'),
    (re.compile(r'\bos\.system\s*\('), 'os.system()', 'MEDIUM',
     'os.system() is vulnerable to command injection — prefer subprocess with a list.'),
    (re.compile(r'\b__import__\s*\('), '__import__()', 'MEDIUM',
     'Dynamic imports via __import__() can execute untrusted code.'),
    (re.compile(r'\bcompile\s*\('), 'compile()', 'MEDIUM',
     'compile() followed by exec could lead to code injection.'),
]

# JavaScript dangerous patterns
JS_DANGEROUS = [
    (re.compile(r'\beval\s*\('), 'eval()', 'HIGH',
     'eval() executes arbitrary JavaScript — a prime XSS attack vector.'),
    (re.compile(r'\.innerHTML\s*='), 'innerHTML assignment', 'HIGH',
     'innerHTML with user data enables XSS — use textContent or DOMPurify.'),
    (re.compile(r'\bdocument\.write\s*\('), 'document.write()', 'MEDIUM',
     'document.write() can overwrite the DOM and enable XSS attacks.'),
    (re.compile(r'\bnew\s+Function\s*\('), 'new Function()', 'HIGH',
     'new Function() is equivalent to eval() and allows arbitrary code execution.'),
    (re.compile(r'\bsetTimeout\s*\(\s*["\']'), 'setTimeout with string', 'MEDIUM',
     'setTimeout with a string argument behaves like eval() — pass a function instead.'),
    (re.compile(r'\bsetInterval\s*\(\s*["\']'), 'setInterval with string', 'MEDIUM',
     'setInterval with a string argument behaves like eval() — pass a function instead.'),
]


def check_dangerous(
    line: str, line_number: int, filepath: str, lang: str = "python"
) -> List[Dict[str, Any]]:
    findings: List[Dict[str, Any]] = []
    patterns = PYTHON_DANGEROUS if lang == "python" else JS_DANGEROUS

    for pattern, name, severity, message in patterns:
        if pattern.search(line):
            findings.append({
                "category": "Dangerous Function",
                "severity": severity,
                "message": f"{name} used — {message}",
                "file": filepath,
                "line": line_number,
                "code": line.strip(),
            })

    return findings

