import streamlit as st
from langchain.document_loaders import TextLoader
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

@st.cache_resource
def load_vector_store():
    docs = []
    for file in ["data/2025_crosstrek_updated.txt", "data/2025_forester.txt"]:
        loader = TextLoader(file)
        docs.extend(loader.load())
    embeddings = OpenAIEmbeddings()
    return FAISS.from_documents(docs, embeddings)

st.title("🚗 Subaru Sales Chatbot")
st.markdown("Ask anything about the **2025 Crosstrek** or **Forester**!")

question = st.text_input("Enter your question:")
if question:
    db = load_vector_store()
    qa = RetrievalQA.from_chain_type(llm=OpenAI(model="gpt-4"), retriever=db.as_retriever())
    answer = qa.run(question)
    st.markdown(f"**Answer:** {answer}")
