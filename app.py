# new code
import os
import streamlit as st
from groq import Groq

# Initialize Groq client with the API key directly
client = Groq(api_key="TOKEN_KEY")  # Replace with your Groq API key

# Updated System prompt for Groq model
system_prompt = """
You are an expert interview coach with 20 years of experience in human resource management. 
Review the user's response to interview questions and provide clear, actionable feedback that focuses on:
1. Relevance: Does the answer directly address the question? Is there unnecessary information?
2. Tone: Is the response confident and professional?
3. Structure: Is the response well-organized? Does it have a clear flow?
4. Vocabulary: Is the vocabulary appropriate for the proficiency level? Avoid overly complex or simplistic words.
Provide only relevant feedback for the user’s proficiency level:
- Beginner (A1): Simple suggestions with easy-to-understand examples.
- Intermediate (B1-B2): A bit more detailed, with room for improvement in vocabulary and structure.
- Advanced (C1): Offer suggestions to refine the response for more precision and clarity.
Please avoid generic feedback like "focus on clarity" if the response is already clear. Provide concrete, useful tips based on the user's input.
"""

# Define a function to generate feedback using the Groq API
def get_feedback(user_response, proficiency_level):
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_response},
            {"role": "system", "content": f"Proficiency Level: {proficiency_level}"}
        ],
        model="llama3-8b-8192"
    )
    return chat_completion.choices[0].message.content

# Streamlit UI
st.title("Job Interview Preparation Assistant")

# Add chatbot flow for asking the user's field
st.subheader("Chatbot Assistant")

user_field = st.text_input("What is your field? (e.g., Software Development, Marketing, Finance)", "")
proficiency_level = st.selectbox("Select Your Proficiency Level:", ["Beginner", "Intermediate", "Advanced"])

if user_field:
    st.write(f"Great! You've selected **{user_field}** as your field.")
    
    # Provide interview questions based on the field
    if user_field.lower() == "software development":
        st.subheader("Interview Questions for Software Development:")
        questions = [
            "Can you explain your experience with coding languages like Python or JavaScript?",
            "How do you handle debugging and troubleshooting in your projects?",
            "What are the most important considerations when working with APIs?"
        ]
    elif user_field.lower() == "marketing":
        st.subheader("Interview Questions for Marketing:")
        questions = [
            "What strategies have you used to increase brand awareness?",
            "Can you explain a successful campaign you worked on and what you learned from it?",
            "How do you approach market research and customer analysis?"
        ]
    elif user_field.lower() == "finance":
        st.subheader("Interview Questions for Finance:")
        questions = [
            "How do you analyze financial statements to assess the health of a company?",
            "What is your experience with financial modeling and forecasting?",
            "Can you explain the concept of risk management in finance?"
        ]
    else:
        st.write("I don't have specific questions for that field yet. Feel free to write your answer to any question!")
        questions = ["Tell us about a challenging project you've worked on and how you handled it."]
    
    # Display one of the questions for the user to answer
    question = st.radio("Select a Question to Answer:", questions)

    # User input area for the answer
    user_response = st.text_area("Your Response", height=200)
    
    # Show submit button
    if st.button("Submit for Feedback"):
        if user_response:
            # Get feedback using the Groq API
            feedback = get_feedback(user_response, proficiency_level)
            st.subheader("Feedback")
            st.write(feedback)

        else:
            st.warning("Please provide a response before submitting.")
else:
    st.write("Please enter your field to get started.")

# old code
# import streamlit as st
# from transformers import pipeline

# # Load the model (Hugging Face model)
# chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

# # Streamlit UI setup
# st.title("Interview-based Chatbot")
# st.write("Ask me any interview-related question in your field!")

# # Text input from user
# user_input = st.text_input("Ask a question:")

# # Generate response when user submits input
# if user_input:
#     response = chatbot(user_input)
#     st.write(f"Chatbot: {response[0]['generated_text']}")
