import argparse
import sys
from anthropic import AnthropicBedrock

def get_summary_stream(text, model_id="anthropic.claude-3-7-sonnet-20250219-v1:0", max_tokens=4096, temperature=1.0):
    client = AnthropicBedrock(
        aws_region="us-west-2",
    )
    
    with client.messages.create(
        model=model_id,
        max_tokens=max_tokens,
        temperature=temperature,
        messages=[
            {
                "role": "user",
                "content": text,
            }
        ],
        stream=True
    ) as stream:
        for chunk in stream:
            if chunk.type == "content_block_delta":
                yield chunk.delta.text

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
    for text_chunk in get_summary_stream(text, args.model, args.max_tokens, args.temperature):
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