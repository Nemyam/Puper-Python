from setuptools import setup, find_packages

setup(
    name="puter",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
        "rich>=10.0.0"
    ],
    author="Nemyam",
    author_email="nemyam0@gmail.com",
    description="A simple Python client for Puter AI API with GPT-4 and Claude support",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Nemyam/Puper-Python",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    keywords="ai, gpt4, claude, puter, chatbot",
) 