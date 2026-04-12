
import os
from typing import List

SUPPORTED_EXTENSIONS = (".js", ".py")

def load_files(path: str) -> List[str]:
    if not os.path.exists(path):
        print(f"[ERROR] Path not found: {path}")
        raise SystemExit(1)

    if os.path.isfile(path):
        if path.endswith(SUPPORTED_EXTENSIONS):
            return [os.path.abspath(path)]
        else:
            print(f"[WARN]  {path} is not a supported file type (.js / .py)")
            return []

    collected: List[str] = []
    for root, _dirs, files in os.walk(path):
        _dirs[:] = [
            d for d in _dirs
            if not d.startswith(".")
            and d not in ("node_modules", "__pycache__", "venv", "env", "dist", "build")
        ]
        for filename in files:
            if filename.endswith(SUPPORTED_EXTENSIONS):
                collected.append(os.path.abspath(os.path.join(root, filename)))

    return sorted(collected)
