# test_run.py
import os
from dotenv import load_dotenv
from config_manager import ConfigManager
from mvp.mvp_pipeline import SummarizationPipeline

load_dotenv()
cfg = ConfigManager()

HF_API_KEY = os.getenv(cfg.get("api_keys", "huggingface"))

pipeline = SummarizationPipeline(HF_API_KEY, cfg)

text = "Machine learning is changing the world rapidly."

print("\n=== Abstractive Summary ===")
print(pipeline.summarize(text, method="abstractive"))

print("\n=== Extractive Summary ===")
print(pipeline.summarize(text, method="extractive"))

print("\n=== Paraphrase ===")
paraphrases = pipeline.paraphrase(text)
for i, p in enumerate(paraphrases, 1):
    print(f"{i}. {p}")
