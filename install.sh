#!/bin/sh
# Installs the /enrich skill for Claude Code.
# Before running: copy the Freckle token Hernán sent you, so it is on your clipboard.
set -e

here="$(cd "$(dirname "$0")" && pwd)"
target="$HOME/.claude/skills/enrich"

if ! python3 -c 1 >/dev/null 2>&1; then
  echo "python3 is missing. Run: xcode-select --install   then run this installer again."
  exit 1
fi

token="$(pbpaste | tr -d '[:space:]')"
if [ "${#token}" -lt 20 ]; then
  echo "The clipboard does not hold the Freckle token. Copy it from Hernán's message and run this again."
  exit 1
fi
security add-generic-password -U -s freckle-enrich -a "$USER" -w "$token"
printf '' | pbcopy

mkdir -p "$target"
if [ "$here" != "$target" ]; then
  cp "$here/SKILL.md" "$here/enrich.py" "$target/"
fi

python3 "$target/enrich.py" --check
echo "Installed. Restart Claude Code, then type /enrich and paste or drop your Sales Navigator screenshots."
