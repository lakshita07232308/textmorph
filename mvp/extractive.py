# mvp/extractive.py
import requests
import logging

logger = logging.getLogger(__name__)

class ExtractiveSummarizer:
    def __init__(self, hf_api_key, model_url):
        self.hf_api_key = hf_api_key
        self.api_url = f"https://api-inference.huggingface.co/models/{model_url}"
        self.headers = {"Authorization": f"Bearer {hf_api_key}"}

    def summarize(self, text, length_params):
        payload = {"inputs": text, "parameters": {**length_params, "do_sample": False, "num_beams": 4}}

        try:
            response = requests.post(self.api_url, headers=self.headers, json=payload, timeout=30)
            response.raise_for_status()
            result = response.json()
            if isinstance(result, list) and len(result) > 0:
                return result[0].get('summary_text', 'No summary generated')
            return str(result)
        except requests.exceptions.RequestException as e:
            logger.error(f"Extractive summarization failed: {e}")
            return f"Error: {str(e)}"
