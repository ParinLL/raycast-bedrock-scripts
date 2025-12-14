"""Generate AWS Cloud Support meeting summary."""
from base_cli import run_cli


def main():
    run_cli(
        description="Generate AWS Cloud Support meeting summary using Claude AI model.",
        prompt_builder=lambda text: f"""我是 Cloud Support 工程師，請幫我總結以下對話大綱，包含 AWS 資源名稱，並回覆給客戶:
---
{text}
---""",
        success_msg="Meeting summary saved to {}"
    )


if __name__ == "__main__":
    main()