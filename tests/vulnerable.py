# tests/vulnerable.py
# Intentionally vulnerable Python file for VulnHawk scanner testing.
# DO NOT use in production.

import os
import pickle
import hashlib
import subprocess

# [HIGH] Hardcoded API key
API_KEY = "sk-U0hPVUxEIE5PVCBCRSBIQVJEQ09ERUQ="

# [HIGH] Hardcoded password
DB_PASSWORD = "super_secret_db_pass123"

# [HIGH] Hardcoded token
AUTH_TOKEN = "token_xyz_9f8e7d6c5b4a3210"

# [HIGH] eval() — arbitrary code execution
def process_input(user_input):
    eval(user_input)

# [HIGH] exec() — arbitrary code execution
def run_code(data):
    exec(data)

# [HIGH] pickle deserialization — RCE risk
def load_data(raw_bytes):
    return pickle.loads(raw_bytes)

# [HIGH] subprocess with shell=True — shell injection risk
def run_command(cmd):
    subprocess.call(cmd, shell=True)

# [MEDIUM] os.system() — command injection risk
def ping_host(host):
    os.system(f"ping {host}")

# [MEDIUM] Weak MD5 hash
weak_hash = hashlib.md5(b"password123").hexdigest()

# [MEDIUM] Weak SHA1 hash
sha1_hash = hashlib.sha1(b"userdata").hexdigest()

