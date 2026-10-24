import sys
import json
import argparse as ap
from pathlib import Path

def main():
    parser = ap.ArgumentParser(description="services description")
    parser.add_argument("--path", required=True)
    args = parser.parse_args()
    file = Path(args.path)
    if file.is_file():
        with open(file, "r") as f:
            x = json.load(f)
            for service in x["services"]:
                print(service["name"], service["port"])
            
    else:
        print(f"{file} does not exist or is not a file")
        sys.exit(1)

if __name__ == "__main__":
    main()