import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from langchain_ollama import OllamaLLM

# ----------------- Streamlit UI -----------------
st.title('🎬 Celebrity Search Results (Local Llama 3)')
input_text = st.text_input("Search the celebrity you want to know about:")

# ----------------- Prompt Templates -----------------
# 1. Ask about celebrity
first_input_prompt = PromptTemplate(
    input_variables=['name'],
    template="Tell me about celebrity {name}"
)

# 2. Ask about date of birth
second_input_prompt = PromptTemplate(
    input_variables=['person'],
    template="When was {person} born?"
)

# 3. Ask about major events
third_input_prompt = PromptTemplate(
    input_variables=['dob'],
    template="Mention 5 major world events that happened around {dob}"
)

# ----------------- Memory Buffers -----------------
person_memory = ConversationBufferMemory(input_key='name', memory_key='chat_history')
dob_memory = ConversationBufferMemory(input_key='person', memory_key='chat_history')
descr_memory = ConversationBufferMemory(input_key='dob', memory_key='description_history')

# ----------------- Local LLM (Ollama) -----------------
llm = OllamaLLM(model="llama3")   # make sure you have `ollama pull llama3`

# ----------------- Chains -----------------
# First chain: celebrity description
chain1 = LLMChain(
    llm=llm,
    prompt=first_input_prompt,
    verbose=True,
    output_key='person',
    memory=person_memory
)

# Second chain: date of birth
chain2 = LLMChain(
    llm=llm,
    prompt=second_input_prompt,
    verbose=True,
    output_key='dob',
    memory=dob_memory
)

# Third chain: major events
chain3 = LLMChain(
    llm=llm,
    prompt=third_input_prompt,
    verbose=True,
    output_key='description',
    memory=descr_memory
)

# Parent sequential chain
parent_chain = SequentialChain(
    chains=[chain1, chain2, chain3],
    input_variables=['name'],
    output_variables=['person', 'dob', 'description'],
    verbose=True
)

# ----------------- Streamlit Execution -----------------
if input_text:
    result = parent_chain({'name': input_text})
    st.write(result)

    with st.expander('Celebrity Info'):
        st.info(person_memory.buffer)

    with st.expander('Major Events'):
        st.info(descr_memory.buffer)
