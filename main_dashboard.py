import streamlit as st
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# 1. WEB PAGE CONFIGURATION (UI Layout)
st.set_page_config(page_title="Student Feedback Analyzer", layout="wide")
st.title("📊 Student Feedback Sentiment Dashboard")
st.markdown("Upload your college student feedback Excel/CSV file to instantly visualize report metrics analytics!")

# 2. CORE ENGINE MODEL LOGIC
def find_sentiment(text):
    blob = TextBlob(str(text))
    score = blob.sentiment.polarity
    if 'could not' in str(text).lower() or 'not understand' in str(text).lower():
        return 'Negative (Bad)'
    if score > 0:
        return 'Positive (Good)'
    elif score < 0:
        return 'Negative (Bad)'
    else:
        return 'Neutral (Average)'

# 3. INTERACTIVE FILE UPLOADER BUTTON
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded file dynamically from local buffer memory grid
    df = pd.read_csv(uploaded_file)
    
    # Process Engine Core application calculation
    df['Analysis_Result'] = df['Feedback'].apply(find_sentiment)
    
    # UI Layout Distribution Splitting Columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📋 Automated Analysis Data Grid")
        st.dataframe(df[['Student_Name', 'Course_Name', 'Feedback', 'Analysis_Result']], use_container_width=True)
        
    with col2:
        st.subheader("📊 Sentiment Percentage Matrix Distribution")
        sentiment_counts = df['Analysis_Result'].value_counts()
        
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', colors=['green', 'red', 'orange'])
        st.pyplot(fig)
        
    st.success("🎉 Web Engine execution completed perfectly! Ready to present your mini-project layout!")
