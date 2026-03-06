#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Ask me Anything
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🤖
# @raycast.argument1 { "type": "text", "placeholder": "Ask me Anything" }

# Documentation:
# @raycast.author Parin Lai
# @raycast.authorURL https://github.com/ParinLL/raycast-bedrock-scripts

source .venv/bin/activate
pdm run source/ask-me-anything.py "${1}"
deactivate