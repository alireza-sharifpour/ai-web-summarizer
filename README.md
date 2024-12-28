# Text Summarization Project

A Python-based text summarization project that leverages modern NLP techniques for generating concise summaries of text content.

## Features

- Text summarization using state-of-the-art models
- Support for multiple AI backends (Ollama, OpenAI)
- Configurable summarization parameters
- Utility functions for text processing

## Project Structure

```
.
├── src/
│   ├── __init__.py
│   ├── main.py          # Application entry point
│   ├── summarizer.py    # Core summarization logic
├── config.py            # Configuration settings
├── requirements.txt     # Project dependencies
└── README.md           # Project documentation
```

## Setup

1. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Unix/macOS
# or
.\venv\Scripts\activate  # On Windows
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Dependencies

Key dependencies include:

- `ollama`: For local AI model integration
- `openai`: For OpenAI API integration
- `pydantic`: For data validation
- `httpx`: For HTTP requests
- `beautifulsoup4`: For text processing

## Usage

Run the main application:

```bash
python src/main.py
```

## Configuration

Adjust settings in `config.py` to customize:

- Model parameters
- API endpoints
- Summarization options

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

