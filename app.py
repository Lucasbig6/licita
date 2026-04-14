from pathlib import Path
import subprocess
import sys


script_path = Path("data") / "data.py"
if script_path.exists():
    subprocess.run([sys.executable, str(script_path)])
