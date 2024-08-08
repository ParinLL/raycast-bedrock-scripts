#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Summarize text with Bedrock
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🤖
# @raycast.argument1 { "type": "text", "placeholder": "Text to be summarized" }

# Documentation:
# @raycast.author Parin Lai
# @raycast.authorURL https://github.com/ParinLL/raycast-bedrock-scripts

source .venv/bin/activate
pdm run source/summarize-text-with-bedrock.py "${1}"
deactivate


