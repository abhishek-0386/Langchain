from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st


## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework

st.title('LangChain Demo With Ollama')
input_text=st.text_input("Search the topic u want")

llm = OllamaLLM(model='llama3.2')

output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    try:
        st.write(chain.invoke({'question': input_text}))
    except Exception as exc:
        st.error(f"Request failed: {exc}")


