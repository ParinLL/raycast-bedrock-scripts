import argparse
import boto3
import json
import sys

def get_summary(text, model_id="anthropic.claude-3-5-sonnet-20240620-v1:0", max_tokens=4096, temperature=1.0):
    client = boto3.client('bedrock-runtime', region_name='us-west-2')
    
    prompt = f"""
    我是 Cloud Support 工程師，請幫我總結以下對話大綱，包含 AWS 資源名稱，並回覆給客戶:
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
    parser.add_argument("text", nargs="?", help="Text to summarize")
    parser.add_argument("-f", "--file", help="Input file containing text to summarize")
    parser.add_argument("-o", "--output", help="Output file to save the summary")
    parser.add_argument("--model", default="anthropic.claude-3-sonnet-20240229-v1:0", help="Model ID to use")
    parser.add_argument("--max-tokens", type=int, default=2048, help="Maximum number of tokens in the response")
    parser.add_argument("--temperature", type=float, default=1.0, help="Temperature for response generation")
    
    args = parser.parse_args()

    if args.file:
        try:
            with open(args.file, 'r', encoding='utf-8') as file:
                text = file.read()
        except FileNotFoundError:
            print(f"Error: File '{args.file}' not found.")
            sys.exit(1)
    elif args.text:
        text = args.text
    else:
        print("Error: Please provide either text or an input file.")
        parser.print_help()
        sys.exit(1)

    summary = ''
    print('\033[97;40m', end="")  # Set text color to white with black background
    for text_chunk in get_summary(text, args.model, args.max_tokens, args.temperature):
        print(text_chunk, end="", flush=True)
        summary += text_chunk
    print('\033[0m')  # Reset text color

    if args.output:
        try:
            with open(args.output, 'w', encoding='utf-8') as file:
                file.write(summary)
            print(f"\nSummary saved to {args.output}")
        except IOError:
            print(f"\nError: Unable to write to file '{args.output}'.")

if __name__ == "__main__":
    main()