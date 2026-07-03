from anthropic import AnthropicBedrock

client = AnthropicBedrock(
    aws_region="ap-northeast-1",
)

message = client.messages.create(
    model="global.anthropic.claude-sonnet-5",
    max_tokens=256,
    messages=[{"role": "user", "content": "Hello, world"}]
)
print(message.content)