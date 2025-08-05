import os
import streamlit as st
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.schema import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
import pickle

DATA_FILES = ["data/2025_crosstrek_updated.txt", "data/2025_forester.txt"]
DB_PATH = "vectorstore/db.pkl"

@st.cache_resource
def load_vector_store():
    if os.path.exists(DB_PATH):
        with open(DB_PATH, "rb") as f:
            return pickle.load(f)

    docs = []
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    for file in DATA_FILES:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            chunks = splitter.split_text(content)
            docs.extend([Document(page_content=chunk) for chunk in chunks])

    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(docs, embeddings)

    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    with open(DB_PATH, "wb") as f:
        pickle.dump(db, f)

    return db

st.title("🚗 Subaru Sales Chatbot")
st.markdown("Ask about the **2025 Crosstrek** or **Forester**.")

question = st.text_input("Enter your question:")
if question:
    db = load_vector_store()
    qa = RetrievalQA.from_chain_type(llm=OpenAI(model="gpt-4"), retriever=db.as_retriever())
    answer = qa.run(question)
    st.markdown(f"**Answer:** {answer}")
