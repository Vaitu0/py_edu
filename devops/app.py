import argparse as ap
import sys
import subprocess
from pathlib import Path

def main():
    parser = ap.ArgumentParser(description="DevOps tools")
    parser.add_argument("--path", required=True, help="Path to the directory")
    args = parser.parse_args()
    directory = Path(args.path)
    if directory.is_dir():
        for element in directory.iterdir():
            if element.is_file():
                print(element.name, element.stat().st_size)
    else:
        print(f"{directory} does not exist or is not a directory")
        sys.exit(1)

    results = subprocess.run(
        ["git", "status", "--short"],
        cwd = directory,
        capture_output=True,
        text=True
    )
    sys.exit(results.returncode)
    
if __name__ == "__main__":
    main()