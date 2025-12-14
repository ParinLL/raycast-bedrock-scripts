"""Translate text to English."""
from base_cli import run_cli


def main():
    run_cli(
        description="Translate text to English using Claude AI model.",
        prompt_builder=lambda text: f"""Please translate the following text into English:
---
{text}
---""",
        success_msg="Translation saved to {}"
    )


if __name__ == "__main__":
    main()