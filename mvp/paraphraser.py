# paraphraser.py
import os
import requests
from dotenv import load_dotenv
import logging

logger = logging.getLogger(__name__)
load_dotenv()

class Paraphraser:
    def __init__(self, api_key=None, model_name="llama-3.1-8b-instant"):
        self.api_key = api_key or os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("❌ GROQ_API_KEY not found in .env")
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        self.model_name = model_name

    def paraphrase(self, text, num_return_sequences=3, temperature=0.9, max_tokens=400):
        if not text.strip():
            return ["⚠️ Please provide valid text."]
        prompt = (
            f"Paraphrase the following text into {num_return_sequences} clean, distinct, "
            f"and natural English sentences. Do NOT include headings, numbers, or explanations:\n\n{text}"
        )
        payload = {
            "model": self.model_name,
            "messages": [
                {"role": "system", "content": "You are a helpful AI that paraphrases text clearly and naturally."},
                {"role": "user", "content": prompt}
            ],
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        try:
            response = requests.post(self.api_url, headers=self.headers, json=payload, timeout=60)
            response.raise_for_status()
            data = response.json()
            text_response = data["choices"][0]["message"]["content"]
            lines = [line.strip() for line in text_response.split("\n") if line.strip()]
            clean_lines = [line for line in lines if not any(line.lower().startswith(x) for x in ["here are", "version", "paraphrase"])]
            return clean_lines[:num_return_sequences]
        except requests.exceptions.RequestException as e:
            logger.error(f"Paraphrasing failed: {e}")
            return [f"❌ Error: {str(e)}"]
