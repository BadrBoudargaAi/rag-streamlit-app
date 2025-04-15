  import streamlit as st
  st.title("RAG Application")
  api_key = st.sidebar.text_input("API Key",type="password")
  uploaded_file = st.sidebar.file_uploader("Upload Document", type=["docx"])
  process_btn = st.sidebar.button("Process")
  if "processed" not in st.session_state:
      st.session_state.processed = False
  if process_btn and uploaded_file:
      st.sidebar.success(f"Document processed: {uploaded_file.name}")
      st.session_state.processed = True
  question = st.text_input("Ask a question:")
  submit = st.button("Submit")
  if submit:
      if not st.session_state.processed:
          st.error("Please process a document first")
      else:
          st.write(f"Demo answer to: {question}")
