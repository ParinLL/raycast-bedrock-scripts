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
# @raycast.author parinll
# @raycast.authorURL https://raycast.com/parinll

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

# # Extract and print the response text in real-time.
# for event in streaming_response["body"]:
#     chunk = json.loads(event["chunk"]["bytes"])
#     if chunk["type"] == "content_block_delta":
#         print(chunk["delta"].get("text", ""), end="")



# try:
#     response = client.invoke_model(
#         body = bytes(json.dumps({
#             "max_tokens": 2048,
#             "temperature": 1.0,
#             "anthropic_version": "bedrock-2023-05-31",
#             "messages": [
#                 {
#                     "role": "user",
#                     "content": [{"type": "text", "text": prompt}],
#                 }
#             ],
#         }), 'utf-8'),
#         modelId = "anthropic.claude-3-haiku-20240307-v1:0",
#         # modelId = "anthropic.claude-instant-v1",
#         contentType = "application/json",
#         accept = "application/json"
#     )
#     response_text = response['body'].read().decode('utf8').strip()
#     response_json = json.loads(response_text)
#     completion = response_json['completion']
#     print('\033[97;40m' + completion + '\033[0m')
# except Exception as e:
#     print('Error invoking endpoint')
#     print(e)
#     sys.exit(1)