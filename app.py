from dotenv import load_dotenv
import os

load_dotenv()

import streamlit as st
from helper import get_pdf_text, get_text_chunks
from vectorstore import create_vector_store, get_relevant_chunks
from llm import get_answer

st.set_page_config("RAG-Based PDF Chatbot", layout="wide")

st.title("RAG-Based PDF Chatbot")


# UPLOAD PDF
pdf_files = st.file_uploader("Upload PDF", accept_multiple_files=True)

vectorstore = None

if pdf_files:
    raw_text = get_pdf_text(pdf_files)
    chunks = get_text_chunks(raw_text)

    vectorstore = create_vector_store(chunks)

    st.success("PDF processed successfully!")


# ASK QUESTION
question = st.text_input("Ask a question from PDF")

if question and vectorstore:
    docs = get_relevant_chunks(vectorstore, question)

    context = " ".join(docs)

    answer = get_answer(context, question)

    st.write("### Answer")
    st.write(answer)