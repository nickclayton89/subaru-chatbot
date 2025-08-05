import streamlit as st
from langchain.schema import Document
from langchain.vectorstores import Chroma
import tempfile
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

@st.cache_resource
def load_vector_store():
    import tempfile
    docs = []
    for file in ["data/2025_crosstrek_updated.txt", "data/2025_forester.txt"]:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            docs.append(Document(page_content=content))

    embeddings = OpenAIEmbeddings()

    # Temporary directory for Chroma persistence
    persist_dir = tempfile.mkdtemp()
    vector_db = Chroma.from_documents(docs, embeddings, persist_directory=persist_dir)
    return vector_db

st.title("🚗 Subaru Sales Chatbot")
st.markdown("Ask anything about the **2025 Crosstrek** or **Forester**!")

question = st.text_input("Enter your question:")
if question:
    db = load_vector_store()
    qa = RetrievalQA.from_chain_type(llm=OpenAI(model="gpt-4"), retriever=db.as_retriever())
    answer = qa.run(question)
    st.markdown(f"**Answer:** {answer}")
