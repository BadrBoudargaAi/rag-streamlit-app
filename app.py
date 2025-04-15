import streamlit as st
from langchain_community.document_loaders import DirectoryLoader, TextLoader, DocxLoader
st.set_page_config(page_title="RAG Demo", layout="wide")
st.title("RAG Application")
st.markdown("Upload documents and ask questions about their content")

# Sidebar for settings
with st.sidebar:
    st.header("Settings")
    model_option = st.selectbox("LLM Provider", ["OpenAI", "Anthropic"])
    api_key = st.text_input(f"{model_option} API Key", type="password")
    st.header("Document Upload")
    uploaded_file = st.file_uploader("Upload Document", type="docx")

   if uploaded_file:
       if st.button("Process Document"):
          st.success(f"Document processed: {uploaded_file.name}")
           st.session_state.doc_processed = True

# Main area
if "doc_processed" not in st.session_state:
    st.session_state.doc_processed = False
if "messages" not in st.session_state:
     st.session_state.messages = []

  # Display existing chat history
  for message in st.session_state.messages:
      with st.chat_message(message["role"]):
          st.write(message["content"])

  # Chat input
  question = st.chat_input("Ask a question about your documents")

  if question:
      # Add user message
      st.session_state.messages.append({"role": "user", "content": question})

      # Display user message
      with st.chat_message("user"):
          st.write(question)

      # Generate response
      with st.chat_message("assistant"):
          if not api_key:
              st.write("Please enter your API key in the sidebar")
          elif not st.session_state.doc_processed:
              st.write("Please upload and process a document first")
          else:
              response = f"This is a demo response to: '{question}'\n\nIn a full RAG implementation, this would retrieve relevant content from your document and generate an accurate answer."
              st.write(response)

              # Add assistant response to history
              st.session_state.messages.append({"role": "assistant", "content": response})
# Add the rest of your app code here with proper indentation
# Make sure there are no leading spaces before any top-level statements
