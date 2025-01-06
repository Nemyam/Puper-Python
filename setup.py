from setuptools import setup, find_packages

setup(
    name="puter",
    version="0.0.12",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
        "rich>=10.0.0"
    ],
    author="Nemyam",
    author_email="nemyam0@gmail.com",
    description="A Python client for Puter AI API - free access to GPT-4 and Claude",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Nemyam/puter",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    keywords="ai, gpt4, claude, puter, chatbot, llm, gpt-4, anthropic",
) 