import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("NEWS_API_KEY")

def get_news_headlines(query, max_articles=5):
    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={query}&language=en&sortBy=publishedAt&pageSize={max_articles}&apiKey={API_KEY}"
    )

    response = requests.get(url)
    if response.status_code != 200:
        print("Error fetching data:", response.text)
        return []

    data = response.json()
    return [article["title"] for article in data.get("articles", [])]
