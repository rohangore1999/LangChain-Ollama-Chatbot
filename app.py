from langchain_core.prompts import ChatPromptTemplate # To give the initial prompt template and set context to the model
from langchain_core.output_parsers import StrOutputParser # Default LLM parser to parse the output from the LLM Model
from langchain_community.llms import Ollama # LLM Model

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# For LangSmith - Observability tracing
# Setting up the environment variables
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# 1) Prompt template
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that can answer questions and help with tasks."), # system prompt: Sets the AI's persona/role - Defines how the AI should behave (helpful, professional, creative, etc.)
        
        ("user", "Question: {question}") # user prompt
    ]
)

# Streamlit framework to show the UI of chatbot seach boxc
st.title("LangChain Demo with Streamlit")
input_text = st.text_input("Enter your question here")

# 2) Model
llm = Ollama(model="llama3.2") # get models from https://ollama.com/search

# It will parse the output from the LLM Model to simple string format
output_parser = StrOutputParser()

# 3) Chain
# Complete LangChain processing pipeline
# prompt_template - Formats the user's question with the system prompt
# llm - Sends the formatted prompt to the language model and gets a response
# output_parser - Converts the LLM's response into a clean string
chain = prompt_template | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text})) # we will give input as "question" which will assign to input_text.