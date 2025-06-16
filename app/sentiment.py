import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Only download once
nltk.download("vader_lexicon")

sia = SentimentIntensityAnalyzer()

def get_sentiment_score(text):
    return sia.polarity_scores(text)
