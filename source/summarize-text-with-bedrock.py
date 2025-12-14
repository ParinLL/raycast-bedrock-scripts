import argparse
import sys
from anthropic import AnthropicBedrock
from config_manager import ConfigManager, default_config
from constants import (
    CLI_DEFAULT_MAX_TOKENS, CLI_DEFAULT_TEMPERATURE,
    ERROR_NO_INPUT, ERROR_FILE_NOT_FOUND, ERROR_WRITE_FAILED,
    OUTPUT_COLOR_START, OUTPUT_COLOR_END
)

def get_summary_stream(text, model_id=None, max_tokens=4096, temperature=1.0, config_manager=None):
    """
    Generate summary stream using Claude model.
    
    Args:
        text: Text to summarize
        model_id: Model ID to use (defaults to ConfigManager default)
        max_tokens: Maximum tokens in response
        temperature: Temperature for generation
        config_manager: ConfigManager instance (defaults to global default)
    
    Yields:
        str: Chunks of summary text
    """
    if config_manager is None:
        config_manager = default_config
    
    if model_id is None:
        model_id = config_manager.get_default_model_id()
    
    # Validate model ID
    if not config_manager.validate_model_id(model_id):
        raise ValueError(f"Invalid model ID: {model_id}")
    
    client = AnthropicBedrock(**config_manager.get_anthropic_client_config())
    
    prompt = f"""Summarize the following text:
---
{text}
---"""
    
    with client.messages.create(
        model=model_id,
        max_tokens=max_tokens,
        temperature=temperature,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        stream=True
    ) as stream:
        for chunk in stream:
            if chunk.type == "content_block_delta":
                yield chunk.delta.text

def main():
    """Main function for summarization CLI."""
    # Initialize configuration manager
    config = default_config
    
    parser = argparse.ArgumentParser(description="Summarize text using Claude AI model.")
    parser.add_argument("text", nargs="?", help="Text to summarize")
    parser.add_argument("-f", "--file", help="Input file containing text to summarize")
    parser.add_argument("-o", "--output", help="Output file to save the summary")
    parser.add_argument("--model", default=config.get_default_model_id(), help="Model ID to use")
    parser.add_argument("--max-tokens", type=int, default=CLI_DEFAULT_MAX_TOKENS, help="Maximum number of tokens in the response")
    parser.add_argument("--temperature", type=float, default=CLI_DEFAULT_TEMPERATURE, help="Temperature for response generation")
    
    args = parser.parse_args()

    # Input validation and loading
    if args.file:
        try:
            with open(args.file, 'r', encoding='utf-8') as file:
                text = file.read()
        except FileNotFoundError:
            print(ERROR_FILE_NOT_FOUND.format(args.file))
            sys.exit(1)
        except UnicodeDecodeError:
            print(f"Error: Unable to decode file '{args.file}'. Please ensure it's UTF-8 encoded.")
            sys.exit(1)
    elif args.text:
        text = args.text
    else:
        print(ERROR_NO_INPUT)
        parser.print_help()
        sys.exit(1)

    # Validate input text
    if not text.strip():
        print("Error: Input text is empty or contains only whitespace.")
        sys.exit(1)

    # Validate model ID if provided
    if args.model != config.get_default_model_id():
        if not config.validate_model_id(args.model):
            print(f"Warning: Model ID '{args.model}' may not be valid. Proceeding anyway.")

    # Process summarization with streaming output
    summary = ''
    print(OUTPUT_COLOR_START, end="")  # Set text color to white with black background
    try:
        for text_chunk in get_summary_stream(text, args.model, args.max_tokens, args.temperature, config):
            print(text_chunk, end="", flush=True)
            summary += text_chunk
    except Exception as e:
        print(OUTPUT_COLOR_END)  # Reset color before error
        print(f"\nError during summarization: {e}")
        sys.exit(1)
    
    print(OUTPUT_COLOR_END)  # Reset text color

    # Save output if requested
    if args.output:
        try:
            with open(args.output, 'w', encoding='utf-8') as file:
                file.write(summary)
            print(f"\nSummary saved to {args.output}")
        except IOError:
            print(ERROR_WRITE_FAILED.format(args.output))

if __name__ == "__main__":
    main()