# src/services/text/sentiment_analysis.py
from transformers import pipeline

class SentimentAnalysisService:
    def __init__(self):
        self.analyzer = pipeline("sentiment-analysis")

    def analyze_sentiment(self, text):
        result = self.analyzer(text)
        return result[0]
