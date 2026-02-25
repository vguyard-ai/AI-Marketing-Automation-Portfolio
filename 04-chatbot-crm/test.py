import anthropic

client = anthropic.Anthropic(api_key="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")

message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=100,
    messages=[{"role": "user", "content": "Dis bonjour en une phrase"}]
)

print(message.content[0].text)
