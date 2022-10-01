#!/usr/bin/env bash
SCRIPT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GIT_ROOT="$(git rev-parse --show-toplevel)"
cd "$GIT_ROOT"

REQUIREMENTS_FILE='requirements-dev.txt'

# Use `python -m pytest` instead of `pytest` to ensure $PWD is appended to sys.path
exec "$SCRIPT_ROOT/tmp-venv.sh" "$REQUIREMENTS_FILE" 'python -m pytest --verbose'