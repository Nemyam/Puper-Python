from puter import ChatCompletion

API_KEY = "your-api-key"

try:
    # using gpt-4o-mini with streaming
    print("\n🤖 GPT-4o-mini streaming:")
    response = ChatCompletion.create(
        messages=[{"role": "user", "content": "yap alot"}],
        model="gpt-4o-mini",
        driver="openai-completion",
        stream=True,
        api_key=API_KEY
    )
    print("\n")  # new line after stream
    
    # using claude with streaming
    print("\n🤖 Claude streaming:")
    response = ChatCompletion.create(
        messages=[{"role": "user", "content": "tell me a quick joke"}],
        model="claude-3-5-sonnet-latest",
        driver="claude",
        stream=True,
        api_key=API_KEY
    )
    print("\n")  # new line after stream
    
except Exception as e:
    print(f"Error: {str(e)}")
