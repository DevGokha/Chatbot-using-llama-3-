import streamlit as st
from langchain_ollama import OllamaLLM

st.title("💬 Local Llama 3 Chatbot (with LangChain)")

# Initialize new OllamaLLM
llm = OllamaLLM(model="llama3")

user_input = st.text_input("Ask me anything:")

if user_input:
    response = llm.invoke(user_input)
    st.write("🤖:", response)


