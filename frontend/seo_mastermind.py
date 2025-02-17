import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

st.set_page_config(page_title="SEO Mastermind", layout="wide")

st.title("🚀 SEO Mastermind - AI-Powered SEO Optimization")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["📖 Readability", "🔑 Keyword Extraction", "😊 Sentiment", "📊 Competitor Analysis", "📈 SEO Trend"])

# 📖 Readability Analysis
with tab1:
    st.header("Web Content Readability Analysis")
    text = st.text_area("Enter your content:")
    if st.button("Analyze Readability"):
        response = requests.post("http://127.0.0.1:5001/readability", json={"text": text})
        readability_score = response.json().get("readability_score", "N/A")
        st.success(f"Readability Score: {readability_score}")

# 🔑 Keyword Extraction
with tab2:
    st.header("Keyword Extraction & Optimization")
    text = st.text_area("Enter content:")
    if st.button("Extract Keywords"):
        response = requests.post("http://127.0.0.1:5002/keywords", json={"text": text})
        keywords = response.json().get("keywords", [])
        st.write(f"Extracted Keywords: {', '.join(keywords)}")
        wordcloud = WordCloud(width=800, height=400).generate(" ".join(keywords))
        st.image(wordcloud.to_array())

# 😊 Sentiment Analysis
with tab3:
    st.header("Sentiment Analysis for Content")
    text = st.text_area("Enter text:")
    if st.button("Analyze Sentiment"):
        response = requests.post("http://127.0.0.1:5003/sentiment", json={"text": text})
        sentiment = response.json().get("sentiment_score", {})
        st.write(sentiment)

# 📊 Competitor Analysis
with tab4:
    st.header("Competitor Analysis using AI")
    query = st.text_input("Enter a keyword:")
    if st.button("Find Competitors"):
        response = requests.post("http://127.0.0.1:5004/competitor", json={"query": query})
        competitors = response.json().get("competitors", [])
        st.write("Top Competitors:", competitors)

# 📈 SEO Trend Prediction
with tab5:
    st.header("SEO Trend Prediction")
    trend_data = st.text_area("Enter historical keyword data (comma-separated):")
    if st.button("Predict Trend"):
        trend_list = list(map(int, trend_data.split(",")))
        response = requests.post("http://127.0.0.1:5005/trend", json={"trend_data": trend_list})
        predicted_trend = response.json().get("predicted_trend", "N/A")
        st.success(f"Predicted Trend Score: {predicted_trend}")
