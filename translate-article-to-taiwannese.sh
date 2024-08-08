#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Translate Article to Taiwannese with Bedrock
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🤖
# @raycast.packageName translateto-Taiwannese
# @raycast.argument1 { "type": "text", "placeholder": "請輸入要翻譯的段落" }

# Documentation:
# @raycast.author Parin Lai
# @raycast.authorURL https://github.com/ParinLL/raycast-bedrock-scripts

source .venv/bin/activate
pdm run source/translate-article-to-taiwannese.py "${1}"
deactivate


