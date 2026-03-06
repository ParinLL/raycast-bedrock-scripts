#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Translate Article to English with Bedrock
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🤖
# @raycast.packageName translateto-English
# @raycast.argument1 { "type": "text", "placeholder": "Articles that need to be translated" }

# Documentation:
# @raycast.author Parin Lai
# @raycast.authorURL https://github.com/ParinLL/raycast-bedrock-scripts

source .venv/bin/activate
pdm run source/translate-article-to-english.py "${1}"
deactivate