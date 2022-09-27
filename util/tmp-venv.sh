#!/usr/bin/env bash
EXECUTED=$(($(return 2>/dev/null)$?))
REQUIREMENTS=${1:?'path to requirements.txt required'}
shift
COMMAND="$@"
REQUIREMENTS_HASH="$(md5sum $REQUIREMENTS | cut -f1 -d' ')"
VENV_DIR="/tmp/venv.$REQUIREMENTS_HASH"
python3 -m venv $VENV_DIR
source $VENV_DIR/bin/activate
echo "Using venv in $VENV_DIR"
pip install -r "$REQUIREMENTS"

if ((EXECUTED)); then
  set -x
  exec $COMMAND
  deactivate
fi