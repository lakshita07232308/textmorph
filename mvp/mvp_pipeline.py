# mvp/mvp_pipeline.py
from .extractive import ExtractiveSummarizer
from .abstractive import AbstractiveSummarizer
from .paraphraser import Paraphraser

class SummarizationPipeline:
    def __init__(self, hf_api_key):
        self.extractive = ExtractiveSummarizer(hf_api_key)
        self.abstractive = AbstractiveSummarizer(hf_api_key)
        self.paraphraser = Paraphraser()

    def summarize(self, text, method='abstractive', length='medium'):
        if method == 'extractive':
            return self.extractive.summarize(text, length)
        else:
            return self.abstractive.summarize(text, length)

    def paraphrase(self, text):
        return self.paraphraser.paraphrase(text)
