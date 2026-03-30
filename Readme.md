## LangChain

## To setup virtual environment
* python -m venv .venv (To install venv)
* Run Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass (Optional if venv fails to activate)
* .venv\Scripts\Activate.ps1

## To install the requirements
* pip install -r requirements.txt

## Setup .env file 
* Add required key in this file

## To run the agents
* streamlit run $filename$.py 

## To load text files as LangChain Documents
* Run `python rag\document_loader.py` to load `rag\documents\sample.txt`
* Or import `load_text_document` / `load_documents_from_folder` from `rag.document_loader`

