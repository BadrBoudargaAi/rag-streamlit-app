import streamlit as st
st.title("RAG Application")
st.sidebar.text_input("API Key",type="password")
st.sidebar.file_uploader("Upload Document")
st.text_input("Ask a question:")
st.button("Submit")
