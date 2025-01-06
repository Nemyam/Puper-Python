# puter-ai

a simple python client for puter.ai api that lets u use gpt-4o-mini and claude models for free!

## installation
```
pip install puter
```

## usage
```python
from puter import ChatCompletion

response = ChatCompletion.create(
    messages=[{"role": "user", "content": "tell me a joke"}],
    model="gpt-4o-mini",
    driver="openai-completion",
    api_key="your-api-key"
)
```
