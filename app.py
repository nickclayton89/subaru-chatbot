import streamlit as st
import os
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.vectorstores import DocArrayInMemorySearch
from langchain.schema import Document
from langchain.chains import RetrievalQA

@st.cache_resource
def load_vector_store():
    docs = []
    for file in ["data/2025_crosstrek_updated.txt", "data/2025_forester.txt"]:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            docs.append(Document(page_content=content))

    embeddings = OpenAIEmbeddings(openai_api_key=os.environ["OPENAI_API_KEY"])
    return DocArrayInMemorySearch.from_documents(docs, embeddings)

st.title("🚗 Subaru Sales Chatbot")
st.markdown("Ask anything about the **2025 Crosstrek** or **Forester**!")

question = st.text_input("Enter your question:")
if question:
    db = load_vector_store()
    qa = RetrievalQA.from_chain_type(llm=OpenAI(model="gpt-4"), retriever=db.as_retriever())
    answer = qa.run(question)
    st.markdown(f"**Answer:** {answer}")
