import requests
import json
import argparse as ap
import sys

def main():
    parser = ap.ArgumentParser(description="HTTP call")
    parser.add_argument("--url", required=True)
    args = parser.parse_args()
    response = requests.get(args.url, timeout=10)
    print(response.status_code)

    if response.status_code != 200:
        print("request failed")
        sys.exit(1)

    data = response.json()
    print(data["name"])





if __name__ == "__main__":
    main()