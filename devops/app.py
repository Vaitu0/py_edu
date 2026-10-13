import argparse as ap
import sys
from pathlib import Path

def main():
    parser = ap.ArgumentParser(description="DevOps tools")
    parser.add_argument("--path", required=True, help="Path to the directory")
    args = parser.parse_args()
    directory = Path(args.path)
    for element in directory.iterdir():
        if element.is_file():
            print(element.name, element.stat().st_size)

if __name__ == "__main__":
    main()