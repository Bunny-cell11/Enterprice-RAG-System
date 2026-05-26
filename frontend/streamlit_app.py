
import streamlit as st
import requests

st.title("Enterprise Secure RAG")

username = st.text_input("Username")
query = st.text_area("Ask a question")

if st.button("Submit"):
    response = requests.get(
        "http://localhost:8000/query",
        params={
            "username": username,
            "query": query
        }
    )

    st.json(response.json())
