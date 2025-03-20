import streamlit as st

st.title("AI Idea Engine 🚀")
st.write("Welcome to the AI-powered idea validation engine!")

idea = st.text_area("Enter your startup idea:")
if idea:
    st.write(f"Analyzing idea: {idea}")
    st.success("This is where AI validation results will be displayed!")
