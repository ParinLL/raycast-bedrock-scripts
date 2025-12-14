"""Translate text to Traditional Chinese."""
from base_cli import run_cli


def main():
    run_cli(
        description="Translate text to Traditional Chinese using Claude AI model.",
        prompt_builder=lambda text: f"""請翻譯以下文字至繁體中文:
---
{text}
---""",
        success_msg="Translation saved to {}"
    )


if __name__ == "__main__":
    main()