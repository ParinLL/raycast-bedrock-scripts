#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Toggle Default Browser
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🌐
# @raycast.packageName Browser Tools

# Documentation:
# @raycast.description Toggle default browser between Brave and Chrome
# @raycast.author parin
# @raycast.authorURL https://github.com/parin

set -euo pipefail

script_dir="$(cd "$(dirname "$0")" && pwd)"
swift_file="$script_dir/source/toggle-default-browser.swift"

if ! /usr/bin/swift "$swift_file"; then
  cat <<'MSG'

Swift runtime failed. This is usually a local Command Line Tools mismatch.

Try:
1) sudo xcode-select --switch /Library/Developer/CommandLineTools
2) sudo rm -rf /Library/Developer/CommandLineTools
3) xcode-select --install

Then run this command again from Raycast.
MSG
  exit 1
fi
