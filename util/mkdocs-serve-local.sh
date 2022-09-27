#!/usr/bin/env bash
SCRIPT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GIT_ROOT="$(git rev-parse --show-toplevel)"
DOC_ROOT="${GIT_ROOT}/docs"

REQUIREMENTS_FILE='requirements-docs.txt'

source "$SCRIPT_ROOT/tmp-venv.sh" "$REQUIREMENTS_FILE"
cd "$DOC_ROOT"

exec mkdocs serve --config-file "$DOC_ROOT/mkdocs.yml" $@