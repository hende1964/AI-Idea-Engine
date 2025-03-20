import streamlit as st
from transformers import pipeline

# Title of the app
st.title("AI Idea Engine 🚀")
st.write("Welcome to the AI-powered idea validation engine!")

# Load GPT model from Hugging Face
gpt_pipeline = pipeline("text-generation", model="gpt2")

# User input for idea validation
idea = st.text_area("Enter your startup idea:")

if st.button("Validate Idea with AI"):
    if idea:
        st.write(f"Analyzing idea: {idea}")
        response = gpt_pipeline(idea, max_length=100, num_return_sequences=1)
        
        # Display AI-generated validation results
        st.success("AI Validation Results:")
        st.write(response[0]['generated_text'])
    else:
        st.warning("Please enter an idea before validating.")


