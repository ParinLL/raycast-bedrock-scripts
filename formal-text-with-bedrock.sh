#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Formal text with Bedrock
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🤖
# @raycast.argument1 { "type": "text", "placeholder": "Text to be Formal" }

# Documentation:
# @raycast.author Parin Lai
# @raycast.authorURL https://github.com/ParinLL/raycast-bedrock-scripts

source .venv/bin/activate
python3 source/formal-text-with-bedrock.py ${1// /%20}
deactivate

