"""Summarize text using Claude AI model."""
from base_cli import run_cli


def main():
    run_cli(
        description="Summarize text using Claude AI model.",
        prompt_builder=lambda text: f"""Summarize the following text:
---
{text}
---""",
        success_msg="Summary saved to {}"
    )


if __name__ == "__main__":
    main()