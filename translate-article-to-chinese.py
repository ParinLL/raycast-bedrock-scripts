#!/Users/parinll/api-scripts/raycast-bedcork/.venv/bin/python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Translate Article to Chinese with Bedrock
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🤖
# @raycast.packageName translateto-Taiwannese
# @raycast.argument1 { "type": "text", "placeholder": "請輸入要翻譯的段落" }

# Documentation:
# @raycast.author Parin Lai
# @raycast.authorURL https://github.com/ParinLL/raycast-bedrock-scripts

import sys
import boto3
import json

client = boto3.client('bedrock-runtime', region_name='us-west-2')
prompt = f"""

請翻譯以下文字至繁體中文:
---
{sys.argv[1]}
---
"""

model_id = "anthropic.claude-3-haiku-20240307-v1:0"
native_request = {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 2048,
    "temperature": 1.0,
    "messages": [
        {
            "role": "user",
            "content": [{"type": "text", "text": prompt}],
        }
    ],
}

# Convert the native request to JSON.
request = json.dumps(native_request)

# Invoke the model with the request.
streaming_response = client.invoke_model_with_response_stream(
    modelId=model_id, body=request
)

for event in streaming_response["body"]:
    chunk = json.loads(event["chunk"]["bytes"])
    if chunk["type"] == "content_block_delta":
        print('\033[97;40m' + chunk["delta"].get("text", "")+ '\033[0m', end="")