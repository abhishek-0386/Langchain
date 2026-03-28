import streamlit as st
from langserve import RemoteRunnable

st.title("LangServe Multi-API Client")

provider = st.selectbox("Choose model", ["gemini", "ollama"])
question = st.text_input("Ask something")

base_url = "http://127.0.0.1:8000"

chains = {
    "gemini": RemoteRunnable(f"{base_url}/gemini/"),
    "ollama": RemoteRunnable(f"{base_url}/ollama/"),
}

if st.button("Submit") and question:
    try:
        result = chains[provider].invoke({"question": question})
        st.write(result)
    except Exception as e:
        st.error(f"Request failed: {e}")
