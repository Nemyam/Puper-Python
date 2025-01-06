# puter 🤖

[![PyPI version](https://badge.fury.io/py/puter.svg)](https://badge.fury.io/py/puter)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple Python client for Puter.AI API that lets you use GPT-4 and Claude models for free!

## Installation
```bash
pip install puter
```

## Quick Start
```python
from puter import ChatCompletion

# Basic completion
response = ChatCompletion.create(
    messages=[{"role": "user", "content": "tell me a joke"}],
    model="gpt-4o-mini",
    driver="openai-completion",
    api_key="your-api-key"
)

# Streaming response
response = ChatCompletion.create(
    messages=[{"role": "user", "content": "tell me a story"}],
    model="claude-3-5-sonnet-latest",
    driver="claude",
    stream=True,
    api_key="your-api-key"
)
```

## Features
- 🚀 OpenAI-style interface
- 🤖 Multiple models supported:
- GPT-4o-mini
- GPT-4o
- Claude 3.5 Sonnet
- 📺 Streaming support
- 🧹 Clean and simple API

## Models & Drivers
| Model | Driver |
|-------|---------|
| gpt-4o-mini | openai-completion |
| gpt-4o | openai-completion |
| claude-3-5-sonnet-latest | claude |

## Version History
- 0.0.12: Updated README
- 0.0.11: Latest release with improved stability
- 0.0.1: Initial release

## License
MIT License - feel free to use in your projects!
