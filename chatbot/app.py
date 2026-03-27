from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

google_api_key = os.getenv("GEMINI_API_KEY")
langsmith_api_key = os.getenv("LANGCHAIN_API_KEY")

if google_api_key:
    os.environ["GOOGLE_API_KEY"] = google_api_key

## Langsmith tracking
if langsmith_api_key:
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_API_KEY"] = langsmith_api_key

## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework

st.title('LangChain Demo With Gemini API')
input_text=st.text_input("Search the topic u want")

if not google_api_key:
    st.error("GEMINI_API_KEY or GOOGLE_API_KEY is missing. Add one to your .env file and restart the app.")
else:
    # Gemini LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",
        google_api_key=google_api_key,
    )
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

    if input_text:
        try:
            st.write(chain.invoke({'question': input_text}))
        except Exception as exc:
            st.error(f"Request failed: {exc}")
