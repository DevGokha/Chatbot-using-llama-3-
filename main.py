import streamlit as st
import os
import google.generativeai as genai

# --- Functions for AI Interaction ---

def get_gemini_response(user_content, task_prompt):
    """
    Sends a request to the Gemini API with user content and a specific task.
    """
    try:
        # Configure the API key from Streamlit secrets
        api_key = st.secrets["GOOGLE_API_KEY"]
        if not api_key:
            st.error("GOOGLE_API_KEY not found. Please set it in your Streamlit secrets.")
            return None

        genai.configure(api_key=api_key)
        
        # Create the prompt for the model
        full_prompt = f"{task_prompt}:\n\n---\n\n{user_content}"
        
        # Initialize and call the Gemini model
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(full_prompt)
        
        return response.text
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# --- Streamlit User Interface ---

st.set_page_config(layout="wide", page_title="Smart Study Buddy")

st.title("🧠 Smart Study Buddy (with Gemini)")
st.write("Paste your text below and I'll help you study!")

# Text input from the user
user_text = st.text_area("Paste your study material here:", height=250)

# Create columns for the buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Summarize Text"):
        if user_text:
            prompt = "Summarize the following text in a few key bullet points."
            with st.spinner("Summarizing..."):
                response = get_gemini_response(user_text, prompt)
                st.subheader("Summary:")
                st.write(response)
        else:
            st.warning("Please paste some text first.")

with col2:
    if st.button("Generate Quiz"):
        if user_text:
            prompt = "Generate a 3-question multiple-choice quiz based on the following text. Provide the correct answer for each question."
            with st.spinner("Generating quiz..."):
                response = get_gemini_response(user_text, prompt)
                st.subheader("Quiz:")
                st.write(response)
        else:
            st.warning("Please paste some text first.")

with col3:
    if st.button("Explain Key Concepts"):
        if user_text:
            prompt = "Identify and explain the top 3 most important key concepts from the following text in simple terms."
            with st.spinner("Explaining concepts..."):
                response = get_gemini_response(user_text, prompt)
                st.subheader("Key Concepts:")
                st.write(response)
        else:
            st.warning("Please paste some text first.")

