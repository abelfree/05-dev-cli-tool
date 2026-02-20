# Developer CLI Utility

A practical Typer-based CLI for project bootstrap and repo stats.

## Commands
- `python -m devtool stats [path]`
- `python -m devtool init <name> [--target path]`

## Quick start
```bash
pip install -r requirements.txt
python -m devtool stats .
python -m devtool init sample-app
```

## Test
```bash
pytest -q
```

## Publish-ready improvements
- Add semantic-release
- Add command plugins
- Add config file support (`.devtool.toml`)