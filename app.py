  import streamlit as st; st.write("Hello, world!")
  st.title("RAG Application")
  st.sidebar.header("Settings")
  api_key = st.sidebar.text_input("API Key", type="password")
