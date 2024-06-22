#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Generate Taiwan Meeting Summarize with Bedrock
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🤖
# @raycast.argument1 { "type": "text", "placeholder": "請輸入需要總結的會議紀錄" }

# Documentation:
# @raycast.author Parin Lai
# @raycast.authorURL https://github.com/ParinLL/raycast-bedrock-scripts

source .venv/bin/activate
python3 source/generate-taiwan-meeting-summarize.py ${1// /%20}
deactivate


