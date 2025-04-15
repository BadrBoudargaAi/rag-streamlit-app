import streamlit as st
  st.title("RAG Demo")

  with st.sidebar:
      st.header("Settings")
      api_key = st.text_input("API Key", type="password")

      st.header("Upload")
      uploaded_file = st.file_uploader("Document", type="docx")

  question = st.text_input("Ask a question:")
  if st.button("Submit"):
      st.write(f"Response: This is a demo answer to: {question}")
