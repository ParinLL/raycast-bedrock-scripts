"""
Base CLI module for Claude Bedrock scripts.
Provides common functionality for all CLI tools.
"""
import argparse
import sys
from typing import Generator, Optional, Callable
from anthropic import AnthropicBedrock
from config_manager import default_config
from constants import (
    CLI_DEFAULT_MAX_TOKENS, CLI_DEFAULT_TEMPERATURE,
    ERROR_NO_INPUT, ERROR_FILE_NOT_FOUND, ERROR_WRITE_FAILED,
    OUTPUT_COLOR_START, OUTPUT_COLOR_END
)


def stream_response(
    text: str,
    model_id: Optional[str] = None,
    max_tokens: int = 4096,
    temperature: float = 1.0
) -> Generator[str, None, None]:
    """
    Stream response from Claude model.
    
    Args:
        text: Input text/prompt
        model_id: Model ID (defaults to config default)
        max_tokens: Maximum tokens in response
        temperature: Temperature for generation
    
    Yields:
        str: Chunks of response text
    """
    config = default_config
    model_id = model_id or config.get_default_model_id()
    
    if not config.validate_model_id(model_id):
        raise ValueError(f"Invalid model ID: {model_id}")
    
    client = AnthropicBedrock(**config.get_anthropic_client_config())
    
    with client.messages.create(
        model=model_id,
        max_tokens=max_tokens,
        temperature=temperature,
        messages=[{"role": "user", "content": text}],
        stream=True
    ) as stream:
        for chunk in stream:
            if chunk.type == "content_block_delta":
                yield chunk.delta.text


def load_input(text_arg: Optional[str], file_arg: Optional[str]) -> str:
    """
    Load input from command line argument or file.
    
    Args:
        text_arg: Direct text input
        file_arg: File path to read from
    
    Returns:
        str: Input text
    """
    if file_arg:
        try:
            with open(file_arg, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print(ERROR_FILE_NOT_FOUND.format(file_arg))
            sys.exit(1)
        except UnicodeDecodeError:
            print(f"Error: Unable to decode file '{file_arg}'. Please ensure it's UTF-8 encoded.")
            sys.exit(1)
    elif text_arg:
        return text_arg
    else:
        print(ERROR_NO_INPUT)
        sys.exit(1)


def save_output(content: str, output_path: str, success_msg: str) -> None:
    """
    Save output to file.
    
    Args:
        content: Content to save
        output_path: File path to save to
        success_msg: Success message to display
    """
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"\n{success_msg}")
    except IOError:
        print(ERROR_WRITE_FAILED.format(output_path))


def run_cli(
    description: str,
    prompt_builder: Callable[[str], str],
    success_msg: str = "Output saved to {}"
) -> None:
    """
    Run CLI with common argument parsing and processing logic.
    
    Args:
        description: CLI description for help text
        prompt_builder: Function that takes input text and returns prompt
        success_msg: Success message template for file output
    """
    config = default_config
    
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("text", nargs="?", help="Text to process")
    parser.add_argument("-f", "--file", help="Input file")
    parser.add_argument("-o", "--output", help="Output file")
    parser.add_argument("--model", default=config.get_default_model_id(), help="Model ID")
    parser.add_argument("--max-tokens", type=int, default=CLI_DEFAULT_MAX_TOKENS, help="Max tokens")
    parser.add_argument("--temperature", type=float, default=CLI_DEFAULT_TEMPERATURE, help="Temperature")
    
    args = parser.parse_args()
    
    # Load and validate input
    text = load_input(args.text, args.file)
    if not text.strip():
        print("Error: Input text is empty or contains only whitespace.")
        sys.exit(1)
    
    # Validate model ID
    if args.model != config.get_default_model_id():
        if not config.validate_model_id(args.model):
            print(f"Warning: Model ID '{args.model}' may not be valid. Proceeding anyway.")
    
    # Build prompt and process
    prompt = prompt_builder(text)
    result = ''
    
    print(OUTPUT_COLOR_START, end="")
    try:
        for chunk in stream_response(prompt, args.model, args.max_tokens, args.temperature):
            print(chunk, end="", flush=True)
            result += chunk
    except Exception as e:
        print(OUTPUT_COLOR_END)
        print(f"\nError during processing: {e}")
        sys.exit(1)
    
    print(OUTPUT_COLOR_END)
    
    # Save output if requested
    if args.output:
        save_output(result, args.output, success_msg.format(args.output))
