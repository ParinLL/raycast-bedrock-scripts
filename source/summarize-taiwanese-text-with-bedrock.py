"""Summarize text in Traditional Chinese."""
from base_cli import run_cli


def main():
    run_cli(
        description="Summarize text in Traditional Chinese using Claude AI model.",
        prompt_builder=lambda text: f"""請以繁體中文總結以下文字:
---
{text}
---""",
        success_msg="Summary saved to {}"
    )


if __name__ == "__main__":
    main()