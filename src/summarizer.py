from bs4 import BeautifulSoup
import requests
from openai import OpenAI
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import OLLAMA_BASE_URL, OLLAMA_API_KEY, MODEL

class WebSummarizer:
    def __init__(self):
        self.client = OpenAI(base_url=OLLAMA_BASE_URL, api_key=OLLAMA_API_KEY)

    def summarize_website(self, url):
        response = requests.get(url, proxies={"http": None, "https": None})
        soup = BeautifulSoup(response.text, 'html.parser')
        text = ' '.join([p.get_text() for p in soup.find_all('p')])

        messages = [
            {"role": "system", "content": "You are a highly skilled text summarizer. Provide clear, concise summaries that capture key points while maintaining readability and context."},
            {"role": "user", "content": f"Summarize this text concisely: {text}"}
        ]

        response = self.client.chat.completions.create(
            model=MODEL,
            messages=messages
        )

        return response.choices[0].message.content