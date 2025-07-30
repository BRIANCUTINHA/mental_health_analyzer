import streamlit as st
from utils.preprocess import clean_text
from utils.predict import predict_sentiment
st.set_page_config(page_title="Mental Health Analyzer")

st.title("🧠 Mental Health Analyzer")
st.markdown("Enter a journal entry, post, or sentence and we'll analyze the sentiment related to mental health.")

# Text input box
user_input = st.text_area("Your Thoughts Here:", height=150)

if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        cleaned = clean_text(user_input)
        prediction, confidence = predict_sentiment(cleaned)
        
        st.subheader("Prediction Result")
        st.success(f"Sentiment: **{prediction}**")
        st.info(f"Confidence: **{confidence:.2f}%**")
