# mvp/mvp_pipeline.py
from .extractive import ExtractiveSummarizer
from .abstractive import AbstractiveSummarizer
from .paraphraser import Paraphraser

class SummarizationPipeline:
    def __init__(self, hf_api_key, config):
        self.extractive = ExtractiveSummarizer(hf_api_key, config.get("models", "extractive"))
        self.abstractive = AbstractiveSummarizer(hf_api_key, config.get("models", "abstractive"))
        self.paraphraser = Paraphraser(model_name=config.get("models", "paraphraser"))

        self.lengths = config.get("summarization", "lengths")
        self.num_paraphrases = config.get("paraphrasing", "num_return_sequences")

    def summarize(self, text, method='abstractive', length='medium'):
        length_params = self.lengths.get(length.lower(), self.lengths["medium"])
        if method.lower() == 'extractive':
            return self.extractive.summarize(text, length_params)
        return self.abstractive.summarize(text, length_params)

    def paraphrase(self, text):
        return self.paraphraser.paraphrase(text, num_return_sequences=self.num_paraphrases)
