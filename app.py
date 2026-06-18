import streamlit as st
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq

@st.cache_resource
def load_rag():

    loader = PyPDFDirectoryLoader("hr_policies")
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=300
    )

    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    return vectorstore

vectorstore = load_rag()

llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    api_key=st.secrets["GROQ_API_KEY"]
)

def ask_bot(question):

    docs = vectorstore.similarity_search(
        question,
        k=5
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    response = llm.invoke(f"""
You are the Zyro Dynamics HR Help Desk Assistant.

Answer ONLY using the provided HR policy context.

If the answer is not available in the context, reply:

I can only answer questions based on Zyro Dynamics HR policy documents.

Context:
{context}

Question:
{question}

Answer:
""")

    return response.content

st.title("Zyro Dynamics HR Help Desk")

question = st.text_input("Ask an HR Question")

if question:
    answer = ask_bot(question)

    st.subheader("HR Bot Response")
    st.write(answer)
