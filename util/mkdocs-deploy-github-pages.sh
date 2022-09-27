#!/usr/bin/env bash
SCRIPT_FILE="$(basename "${BASH_SOURCE[0]}")"
SCRIPT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GIT_ROOT="$(git rev-parse --show-toplevel)"

REQUIREMENTS_FILE='requirements-docs.txt'
GH_PAGES_BRANCH='gh-pages'

source "$SCRIPT_ROOT/tmp-venv.sh" "$REQUIREMENTS_FILE"

export _TMP=$(mktemp -d)
trap "rm -rf $_TMP" EXIT

cd "$GIT_ROOT/docs" 

mkdocs gh-deploy \
  --config-file "$GIT_ROOT/docs/mkdocs.yml" \
  --site-dir $_TMP \
  --remote-branch $GH_PAGES_BRANCH \
  --message "$(date) - ${SCRIPT_FILE}"\
  --clean \
  --no-history \
  --verbose