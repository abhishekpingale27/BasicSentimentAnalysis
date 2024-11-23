import streamlit as st
from app.sentiment_analysis import analyze_sentiment

# Streamlit app UI
st.title("Basic Sentiment Analysis Application")
st.write("Enter your text below, and the app will classify the sentiment.")

# User Input
user_input = st.text_area("Input Text", placeholder="Type your text here...")

# Analyze Sentiment
if st.button("Analyze Sentiment"):
    if user_input:
        sentiment = analyze_sentiment(user_input)
        st.success(f"The sentiment is: **{sentiment}**")
    else:
        st.warning("Please enter some text to analyze.")
