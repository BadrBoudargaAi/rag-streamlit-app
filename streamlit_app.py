import streamlit as st

  st.set_page_config(page_title="RAG Demo", layout="wide")

  # App title and description
  st.title("🔍 RAG Application Demo")
  st.markdown("Upload documents and ask questions about their content")

  # Sidebar for settings
  with st.sidebar:
      st.header("Settings")

      # LLM selection
      llm_provider = st.selectbox("LLM Provider", ["OpenAI", "Anthropic"])
      api_key = st.text_input(f"{llm_provider} API Key", type="password")

      # Document section
      st.header("Documents")
      uploaded_file = st.file_uploader("Upload Document", type="docx")

      if uploaded_file and st.button("Process Document"):
          st.success(f"Processed document: {uploaded_file.name}")

  # Main area
  if "messages" not in st.session_state:
      st.session_state.messages = []

  # Display chat history
  for message in st.session_state.messages:
      with st.chat_message(message["role"]):
          st.write(message["content"])

  # Chat input
  prompt = st.chat_input("Ask a question about your documents")
  if prompt:
      # Add user message to history
      st.session_state.messages.append({"role": "user", "content": prompt})

      # Display user message
      with st.chat_message("user"):
          st.write(prompt)

      # Generate response
      with st.chat_message("assistant"):
          if not api_key:
              st.write("Please enter your API key in the settings panel")
          else:
              response = f"This is a demo response to: '{prompt}'\n\nIn a real RAG application, this would search the document and generate a response based on its content."
              st.write(response)

              # Add assistant response to history
              st.session_state.messages.append({"role": "assistant", "content": response})
