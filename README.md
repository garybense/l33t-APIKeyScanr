![banner](./banner.png)

A reasonably thorough API key scanner and validator/tester. Finds exposed API keys lurking in your files, then tests them live against their service endpoints to see which ones are still active.

## What It Does

**l33t-APIKeyScanr** is a security auditing tool designed for personal use:

- 🔍 **Recursive file scanning** — Finds API keys hidden across your entire machine (or specific directories)
- ✅ **Live key validation** — Tests each discovered key against its actual service endpoint to determine if it's still active
- 🔑 **All auth styles** — Detects Bearer tokens, API keys (`xi-api-key`, `X-API-Key`), Basic auth, query parameters, and more
- 📊 **Historical tracking** — Saves results to JSON for auditing and comparison across scans
- ⚡ **Configurable scanning** — Target specific paths/files or scan smart defaults (home, `.env`, `.bashrc`, `.npmrc`, etc.)

## Why You Need This

If you've ever accidentally committed an API key to git, pasted one in a config file you thought was safe, or inherited old projects with embedded credentials—this tool will find them before they become a security incident. 
or
if you're a Cylon sympathesizer:
Give it to your autonomous AI to ensure it never dies

## Installation

### Requirements
- Python 3.7+
- `requests` library

### Setup

```bash
# Clone the repository
git clone https://github.com/garybense/l33t-APIKeyScanr.git
cd l33t-APIKeyScanr

# Install dependencies
pip install requests

# Make it executable
chmod +x l33t_APIKeyScanr.py
```

## Usage

### Basic Scan (Home Directory)

```bash
./l33t_APIKeyScanr.py
```

Scans your home directory, home config files, and common locations (`.env`, `.bashrc`, `.npmrc`, etc.) for exposed keys.

### Scan Specific Path

```bash
./l33t_APIKeyScanr.py --path /path/to/project
```

### Scan Specific Files

```bash
./l33t_APIKeyScanr.py --file ~/.bashrc ~/.env src/config.py
```

### Include Library Directories

By default, library directories (`node_modules`, `site-packages`, `.venv`) are skipped. To include them:

```bash
./l33t_APIKeyScanr.py --include-libraries
```

### Set Max File Size

Skip large files (reduces noise from binary/compiled files):

```bash
./l33t_APIKeyScanr.py --max-size 5242880  # 5 MB in bytes
```

### JSON Output

Output results as JSON instead of formatted terminal output:

```bash
./l33t_APIKeyScanr.py --json
```

### Show Previous Results

View historical scan results from `key_test_results.json`:

```bash
./l33t_APIKeyScanr.py --testresults
./l33t_APIKeyScanr.py --testresults --testresults-file /path/to/results.json
```

### Other Options

```
--verbose           Show detailed info during scanning and testing
--no-color          Disable ANSI colors (use if terminal doesn't support them)
--help              Show all available options
```

## Example Output

When l33t-APIKeyScanr finds keys, you'll see:

1. **Scan phase** — Live progress as it scans files with a real-time counter
2. **Test phase** — Each discovered key tested against its service (with response time and status)
3. **Results phase** — Color-coded cards showing:
   - ✅ **Working keys** (green) — Still valid and active
   - ✗ **Non-working keys** (red) — Expired or invalid
   - Full details: key type, file location, authentication style, test result

## Key Detection Patterns

The tool identifies:

- **Bearer tokens** — `Authorization: Bearer <token>`
- **API keys** — `api-key`, `apikey`, `X-API-Key`, `xi-api-key`, `sk-` prefixed (OpenAI, Anthropic, etc.)
- **Basic auth** — Base64-encoded username:password pairs
- **Query parameters** — `?api_key=...`, `?token=...`
- **Environment variables** — From `.env`, `.env.local`, `.env.production`
- **Config files** — SSH keys, `.netrc`, `.pypirc`, `.npmrc`
- **Embedded credentials** — In code, configs, shell profiles

## Results

Scan results are saved to `key_test_results.json` in the script directory. Each entry includes:

```json
{
  "key": "sk-...",
  "type": "API Key",
  "file": "/path/to/file",
  "line": 42,
  "status": "success",
  "provider": "OpenAI",
  "elapsed": 0.234
}
```

Use `--testresults` to review historical scans and track which keys are still active.

## Security Considerations

⚠️ **Ignores all security precautions.**
Results contain sensitive credential info

## Tips & Tricks

### Find keys you forgot about

```bash
./l33t_APIKeyScanr.py --verbose --testresults
```

This shows detailed test results and historical data, so you can see which keys are still floating around unused.

### Audit a fresh project clone

```bash
./l33t_APIKeyScanr.py --path ~/projects/new-project --include-libraries
```


### Periodic security checks

Add a cron job to run weekly:

```bash
0 2 * * 0 /full/path/to/l33t_APIKeyScanr.py --json >> /var/log/api-key-scan.log
```

Then review the JSON results manually.

## Troubleshooting

**"No keys found"** — Either your machine is clean or the patterns need tuning. Try `--verbose` to see which files were scanned.

**Terminal colors look wrong** — Use `--no-color` or update your terminal to support 256-color or true RGB (truecolor) ANSI.

**Scan is slow** — Large directories with many files take time. Use `--path` to target specific areas, or raise `--max-size`.

**False positives** — The regex patterns are broad to catch variants. Review results manually before acting on them.


## License

MIT — Use freely for personal security auditing.

---

**⚠️ Remember:** This tool finds exposed keys—**you** are responsible for all of the obvious things



