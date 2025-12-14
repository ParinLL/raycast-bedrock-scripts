"""Paraphrase text in a formal and logical way."""
from base_cli import run_cli


def main():
    run_cli(
        description="Paraphrase text in a formal and logical way using Claude AI model.",
        prompt_builder=lambda text: f"""Please help me paraphrase the following text in a formal and logical way:
---
{text}
---""",
        success_msg="Formal text saved to {}"
    )


if __name__ == "__main__":
    main()