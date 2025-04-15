import streamlit as st
from utils.pdf_loader import load_and_chunk_pdfs
from utils.vector_store import create_or_load_vector_store, search_docs
from utils.qa_engine import ask_llm
import os

st.set_page_config(page_title="DocuChat Pro", layout="wide")
st.title("📄🤖 DocuChat Pro – Chat with Multiple PDFs")

uploaded_files = st.file_uploader("Upload your PDFs", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    with st.spinner("Processing PDFs..."):
        texts = load_and_chunk_pdfs(uploaded_files)
        vectordb = create_or_load_vector_store(texts)
        st.success("PDFs processed! Ask me anything about them.")

    query = st.text_input("Ask a question about your PDFs:")
    if query:
        with st.spinner("Thinking..."):
            docs = search_docs(vectordb, query)
            response = ask_llm(docs, query)
            st.markdown("### 🧠 Answer")
            st.write(response)


