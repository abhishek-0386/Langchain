from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from fastapi import FastAPI
from langserve import add_routes
import uvicorn
import os

from dotenv import load_dotenv
load_dotenv()

google_api_key=os.getenv('GEMINI_API_KEY')
langsmith_api_key = os.getenv("LANGCHAIN_API_KEY")

## Google API Key
if google_api_key:
    os.environ['GOOGLE_API_KEY']= google_api_key

## Langsmith tracking
if langsmith_api_key:
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_API_KEY"] = langsmith_api_key

app = FastAPI(title="Multi API LangServe")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("user", "Question: {question}")
    ]
)

parser = StrOutputParser()

gemini_chain = (
    prompt
    | ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",
        google_api_key=os.getenv("GEMINI_API_KEY"),
    )
    | parser
)

ollama_chain =(
    prompt
    | OllamaLLM(model='llama3.2')
    | parser
)

add_routes(app, gemini_chain, path="/gemini")
add_routes(app, ollama_chain, path='/ollama')

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)