"""Ask Claude AI model anything."""
from base_cli import run_cli


def main():
    run_cli(
        description="Ask Claude AI model anything.",
        prompt_builder=lambda text: text,
        success_msg="Response saved to {}"
    )


if __name__ == "__main__":
    main()