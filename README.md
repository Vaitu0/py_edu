# py_edu

Small Python exercises for DevOps-style scripts. Each script reads an argument, does one job, and exits with code `1` when that job fails.

Run the commands from the `devops` directory.

## `app.py`

Lists the files in a directory and the size of each file in bytes. Then it runs `git status --short` in that directory and exits with git's exit code.

```bash
python3 app.py --path .
```

A missing path, or a path that is not a directory, prints an error and exits with code `1`.

## `services.py`

Reads a JSON file and prints each service name and port. The sample data is in `services.json`.

```bash
python3 services.py --path services.json
```

A missing file, or a path that is not a file, prints an error and exits with code `1`.

## `check_url.py`

Sends an HTTP GET request and prints the status code. When the status is `200`, it also prints the `name` field from the JSON reply. This script needs the `requests` package.

```bash
python3 check_url.py --url https://jsonplaceholder.typicode.com/users/1
```

Any status other than `200` prints `request failed` and exits with code `1`.
