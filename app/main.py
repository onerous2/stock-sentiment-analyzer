import streamlit as st
from app.fetch_data import get_news_headlines
from app.sentiment import get_sentiment_score

st.set_page_config(page_title="Stock Sentiment Analyzer")
st.title("📈 Stock Sentiment Analyzer")
st.markdown("Type a stock ticker or company name to analyze news sentiment in real time.")

# Input
company = st.text_input("Enter a company name or stock ticker:", value="Apple")

if company:
    st.info(f"Fetching sentiment for: {company}")

    # Fetch news
    headlines = get_news_headlines(company)

    if not headlines:
        st.warning("No news headlines found.")
    else:
        # Analyze sentiment
        sentiment_scores = [get_sentiment_score(headline)["compound"] for headline in headlines]

        # Output results
        for headline, score in zip(headlines, sentiment_scores):
            st.write(f"\n📰 {headline}")
            st.progress((score + 1) / 2)  # Normalize from [-1,1] to [0,1]

        avg_score = sum(sentiment_scores) / len(sentiment_scores)

        # Recommendation
        st.subheader("🔍 Overall Sentiment:")
        if avg_score > 0.2:
            st.success("✅ Positive outlook")
        elif avg_score < -0.2:
            st.error("⚠️ Negative sentiment — Caution")
        else:
            st.info("➖ Neutral sentiment")
