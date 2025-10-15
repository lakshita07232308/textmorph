# test_run.py
import os
from dotenv import load_dotenv
from mvp.mvp_pipeline import SummarizationPipeline

load_dotenv()
hf_api_key = os.getenv("HF_API_KEY")
if not hf_api_key:
    print("Please set HF_API_KEY in your .env file")
    exit()

pipeline = SummarizationPipeline(hf_api_key)

text = "Machine learning is a subset of artificial intelligence that enables systems to learn and improve from experience without being explicitly programmed."

print("=== Abstractive Summary ===")
print(pipeline.summarize(text, method='abstractive', length='short'))

print("\n=== Extractive Summary ===")
print(pipeline.summarize(text, method='extractive', length='short'))

print("\n=== Paraphrase ===")
for i, p in enumerate(pipeline.paraphrase(text), 1):
    print(f"{i}. {p}")
