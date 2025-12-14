"""
Shared constants for Claude Sonnet Upgrade Testing

Central location for model IDs, regions, and default parameters.
"""

# Model Configuration
LATEST_APAC_CLAUDE_SONNET_4 = "anthropic.claude-sonnet-4-5-20250929-v1:0"
GLOBAL_CLAUDE_SONNET_4 = "global.anthropic.claude-sonnet-4-5-20250929-v1:0"

# Regional Configuration
APAC_REGION = "ap-northeast-1"
US_WEST_REGION = "us-west-2"
US_EAST_REGION = "us-east-1"
DEFAULT_REGION = "ap-northeast-1"

# Default Parameters
DEFAULT_MAX_TOKENS = 4096
DEFAULT_TEMPERATURE = 1.0
DEFAULT_ANTHROPIC_VERSION = "bedrock-2023-05-31"

# CLI Defaults
CLI_DEFAULT_MAX_TOKENS = 2048
CLI_DEFAULT_TEMPERATURE = 1.0

# Validation Constants
VALID_OPERATIONS = ["translate", "summarize", "ask"]

# Error Messages
ERROR_NO_INPUT = "Error: Please provide either text or an input file."
ERROR_FILE_NOT_FOUND = "Error: File '{}' not found."
ERROR_WRITE_FAILED = "Error: Unable to write to file '{}'."
ERROR_INVALID_MODEL = "Error: Invalid model ID: {}"
ERROR_INVALID_REGION = "Error: Invalid region: {}"

# Output Formatting
OUTPUT_COLOR_START = '\033[97;40m'  # White text on black background
OUTPUT_COLOR_END = '\033[0m'        # Reset color