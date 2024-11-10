import streamlit as st
from transformers import pipeline

# Load the model (Hugging Face model)
chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

# Streamlit UI setup
st.title("Interview-based Chatbot")
st.write("Ask me any interview-related question in your field!")

# Text input from user
user_input = st.text_input("Ask a question:")

# Generate response when user submits input
if user_input:
    response = chatbot(user_input)
    st.write(f"Chatbot: {response[0]['generated_text']}")
