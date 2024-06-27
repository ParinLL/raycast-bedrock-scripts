import argparse
import boto3
import json

def get_summary(text, model_id="anthropic.claude-3-haiku-20240307-v1:0", max_tokens=2048, temperature=1.0):
    client = boto3.client('bedrock-runtime', region_name='us-west-2')
    
    prompt = f"""
    Please translate the following text into English:
    ---
    {text}
    ---"""
    
    request = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": max_tokens,
        "temperature": temperature,
        "messages": [
            {
                "role": "user",
                "content": [{"type": "text", "text": prompt}],
            }
        ],
    })

    response = client.invoke_model_with_response_stream(modelId=model_id, body=request)
    
    for event in response["body"]:
        chunk = json.loads(event["chunk"]["bytes"])
        if chunk["type"] == "content_block_delta":
            yield chunk["delta"].get("text", "")

def main():
    parser = argparse.ArgumentParser(description="Summarize text using Claude AI model.")
    parser.add_argument("text", help="Text to summarize")
    parser.add_argument("--model", default="anthropic.claude-3-haiku-20240307-v1:0", help="Model ID to use")
    parser.add_argument("--max-tokens", type=int, default=2048, help="Maximum number of tokens in the response")
    parser.add_argument("--temperature", type=float, default=1.0, help="Temperature for response generation")
    
    args = parser.parse_args()

    print('\033[97;40m', end="")  # Set text color to white with black background
    for text_chunk in get_summary(args.text, args.model, args.max_tokens, args.temperature):
        print(text_chunk, end="", flush=True)
    print('\033[0m')  # Reset text color

if __name__ == "__main__":
    main()