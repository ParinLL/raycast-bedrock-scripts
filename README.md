# AWS Bedrock Claude Scripts

A collection of Python scripts utilizing AWS Bedrock Claude Sonnet 4.5 model, providing various text processing capabilities including translation, summarization, and text formalization.

## Features

- **Ask Me Anything** - Ask Claude AI any question
- **Text Formalization** - Rewrite text into formal and logically clear versions
- **Meeting Summarization** - Generate summaries for meetings
- **Translation** - Bidirectional translation between English and Traditional Chinese
- **Text Summarization** - Generate text summaries in Traditional Chinese
- **Streaming Output** - All features support real-time streaming responses

## System Requirements

- Python 3.12
- PDM (Python Development Master) - Python package manager
- AWS account with Bedrock access permissions
- Configured AWS credentials (via AWS CLI or environment variables)

## Installation

### 1. Install PDM

PDM is the recommended package manager for this project. Install it using:

```bash
# macOS/Linux
curl -sSL https://pdm-project.org/install-pdm.py | python3 -

# Or using pip
pip install --user pdm

# Or using Homebrew (macOS)
brew install pdm
```

For more installation options, visit: https://pdm-project.org/latest/#installation

### 2. Clone and Setup

```bash
git clone <repository-url>
cd raycast-bedrock-scripts

# Install dependencies using PDM
pdm install
```

### 3. Running Scripts with PDM

Use PDM to run scripts in the managed environment:

```bash
# Run any script using pdm run
pdm run python source/ask-me-anything.py "Your question"

# Or activate the virtual environment
eval $(pdm venv activate)
python source/ask-me-anything.py "Your question"
```

## AWS Configuration

Ensure your AWS credentials are properly configured with permissions to access Bedrock services.

View available Anthropic models:
```bash
aws bedrock list-foundation-models --region=us-west-2 --by-provider anthropic --query "modelSummaries[*].modelId"
```

**Default Model**: The scripts use `global.anthropic.claude-sonnet-4-5-20250929-v1:0` (Claude Sonnet 4.5) by default in the `ap-northeast-1` region.

## Usage

**Note**: All commands below can be prefixed with `pdm run` to use the PDM-managed environment:
```bash
pdm run python source/script-name.py [arguments]
```

### 1. Ask Me Anything

Ask Claude AI any question:

```bash
# Direct question input
pdm run python source/ask-me-anything.py "What is AWS Lambda?"

# Read question from file
pdm run python source/ask-me-anything.py -f question.txt

# Save response to file
pdm run python source/ask-me-anything.py "Explain Docker" -o answer.txt

# Using shell script
./ask-me-anything.sh "Your question here"
```

### 2. Text Formalization

Rewrite text into formal and logically clear versions:

```bash
# Direct text input
pdm run python source/formal-text-with-bedrock.py "casual text here"

# Read from file
pdm run python source/formal-text-with-bedrock.py -f input.txt -o formal.txt

# Using shell script
./formal-text-with-bedrock.sh "text to formalize"
```

### 3. Meeting Summarization

Generate summaries for AWS Cloud Support meetings:

```bash
# Read meeting notes from file
pdm run python source/generate-taiwan-meeting-summarize.py -f meeting.txt

# Save summary
pdm run python source/generate-taiwan-meeting-summarize.py -f meeting.txt -o summary.txt

# Using shell script
./generate-taiwan-meeting-summarize.sh
```

### 4. Translation

#### Translate to English:
```bash
# Translate Traditional Chinese to English
pdm run python source/translate-article-to-english.py "要翻譯的中文文字"

# Translate from file
pdm run python source/translate-article-to-english.py -f chinese.txt -o english.txt

# Using shell script
./translate-article-to-english.sh
```

#### Translate to Traditional Chinese:
```bash
# Translate English to Traditional Chinese
pdm run python source/translate-article-to-taiwannese.py "Text to translate"

# Translate from file
pdm run python source/translate-article-to-taiwannese.py -f english.txt -o chinese.txt

# Using shell script
./translate-article-to-taiwannese.sh
```

### 5. Text Summarization (Traditional Chinese)

Generate Traditional Chinese summaries:

```bash
# Direct text input
pdm run python source/summarize-taiwanese-text-with-bedrock.py "長篇文字內容"

# Read from file
pdm run python source/summarize-taiwanese-text-with-bedrock.py -f article.txt -o summary.txt

# Using shell script
./summarize-taiwanese-text-with-bedrock.sh
```

## Advanced Options

All scripts support the following options:

```bash
--model MODEL_ID          # Specify model ID to use
--max-tokens N            # Set maximum tokens for response (default: 4096)
--temperature T           # Set generation temperature (default: 1.0)
-f, --file FILE          # Read input from file
-o, --output FILE        # Save output to file
```

Example:
```bash
pdm run python source/ask-me-anything.py \
  --model global.anthropic.claude-sonnet-4-5-20250929-v1:0 \
  --max-tokens 2048 \
  --temperature 0.7 \
  -f input.txt \
  -o output.txt
```

## Project Structure

```
.
├── source/
│   ├── base_cli.py                             # Base CLI framework (shared logic)
│   ├── ask-me-anything.py                      # Q&A system
│   ├── formal-text-with-bedrock.py            # Text formalization
│   ├── generate-taiwan-meeting-summarize.py   # Meeting summarization
│   ├── translate-article-to-english.py        # Translate to English
│   ├── translate-article-to-taiwannese.py     # Translate to Traditional Chinese
│   ├── summarize-taiwanese-text-with-bedrock.py # Traditional Chinese summarization
│   ├── AnthropicBedrock.py                    # Generic summarization
│   ├── config_manager.py                       # Configuration management
│   ├── constants.py                            # Constants definition
│   └── test_cli.py                             # Test suite
├── *.sh                                        # Shell script wrappers
├── pyproject.toml                              # PDM project configuration
├── pdm.lock                                    # PDM lock file
└── README.md                                   # This file
```

## Development

### Running Tests

```bash
pdm run python source/test_cli.py
```

### Adding New Dependencies

```bash
pdm add package-name
```

### Updating Dependencies

```bash
pdm update
```

## Dependencies

This project uses PDM for dependency management. All dependencies are defined in `pyproject.toml`:

- `boto3` - AWS SDK for Python
- `anthropic[bedrock]` - Anthropic Claude SDK with Bedrock support
- `argparse` - Command-line argument parsing

PDM automatically manages the virtual environment and ensures consistent dependency versions across all environments.

## Important Notes

- All scripts use streaming output for real-time response viewing
- Input text must be UTF-8 encoded
- Ensure AWS credentials have sufficient permissions to access Bedrock services
- Using Bedrock services incurs costs - monitor your usage

## Error Handling

Scripts include comprehensive error handling:
- File existence checks
- UTF-8 encoding validation
- Empty input validation
- Model ID validation
- API error handling

## License

Please refer to the project license documentation.

## Contributing

Issues and Pull Requests are welcome.

