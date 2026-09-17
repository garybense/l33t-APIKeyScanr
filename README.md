# l33t_APIKeyScanr

Elite API Key Scanner & Tester — scans the filesystem for API keys and tests them live.

Supports Bearer, Header, Query, Basic, and Body authentication methods. Detects OpenAI, Anthropic, Google, GitHub, AWS, NVIDIA, Docker, and many other key types.

## Quick Start

```bash
# Scan and test keys from the home directory
python3 l33t_APIKeyScanr.py

# Scan a specific file
python3 l33t_APIKeyScanr.py -f config.json

# Scan a specific path with verbose output
python3 l33t_APIKeyScanr.py -p /path/to/code -v

# Output results as JSON
python3 l33t_APIKeyScanr.py -p /Users/me -j

# View previously saved test results without scanning
python3 l33t_APIKeyScanr.py --testresults

# View saved results with full key details
python3 l33t_APIKeyScanr.py --testresults -v

# Use a custom results file
python3 l33t_APIKeyScanr.py --testresults --testresults-file /path/to/results.json
```

## Features

- **Filesystem scanning** — searches files for API key patterns
- **Live key testing** — validates keys against provider endpoints
- **False positive filtering** — advanced filtering for AWS CLI help text, SDK parameters, test fixtures, sequential patterns, and more
- **Multiple provider support** — OpenAI, Anthropic, Google, GitHub, AWS, NVIDIA, Docker, etc.
- **Saved result viewing** — `--testresults` flag replays results from `key_test_results.json`
- **JSON output** — `-j` flag for machine-readable results

## CLI Options

| Flag | Description |
|------|-------------|
| `-p, --path` | Path to scan (can be specified multiple times) |
| `-f, --file` | Specific file to scan |
| `-v, --verbose` | Show full key details and verbose error messages |
| `-j, --json` | Output results as JSON |
| `--no-color` | Disable colored output |
| `--max-size` | Maximum file size to scan in bytes (default: 5000000) |
| `--include-libraries` | Include node_modules and vendor directories |
| `--testresults` | Display saved test results from `key_test_results.json` |
| `--testresults-file` | Custom path to results JSON file |

## How It Works

1. **Scan Phase**: Walks the filesystem looking for API key patterns
2. **Filter Phase**: Applies `filter_false_positives` to remove SDK parameters, AWS CLI help text, test fixtures, sequential patterns, and other false positives
3. **Test Phase**: Tests each remaining key against its provider's endpoint
4. **Output Phase**: Displays working vs non-working keys, saves results to `key_test_results.json`

## Files

- `l33t_APIKeyScanr.py` — the scanner & tester
- `key_test_results.json` — saved test results (gitignored)
- `.gitignore` — excludes secrets and temp files

## Security

- Results are saved locally to `key_test_results.json` (gitignored)
- Keys are displayed in terminal output for sysadmin review
- Review found keys carefully and rotate any that shouldn't be in plaintext storage

## License

MIT
