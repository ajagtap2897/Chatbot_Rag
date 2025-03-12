import streamlit as st
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import ChatOllama
from langchain.chains import RetrievalQA
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter, CharacterTextSplitter
from langchain_community.document_loaders import CSVLoader

# Load environment variables if needed
# from dotenv import load_dotenv
# load_dotenv()

@st.cache_resource
def initialize_qa_system():
    # Initialize Ollama embeddings
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    
    # Initialize FAISS index
    index_path = "faiss_index"
    file_path = ("D:/Python/langchain_Rag/Wolrd Population Data.csv")
    if os.path.exists(index_path):
        db = FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)
    else:
        # Load and split documents
        file_ext = os.path.splitext(file_path)[1].lower()
        if file_ext == ".txt":
            loader = TextLoader(file_path)
            text_splitter = CharacterTextSplitter(
                chunk_size=1500,
                chunk_overlap=200
            )
        elif file_ext == ".csv":
            loader = CSVLoader(file_path)
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=500,
                chunk_overlap=200
            )    
        
        documents = loader.load()

        docs = text_splitter.split_documents(documents)
        db = FAISS.from_documents(docs, embeddings)
        db.save_local(index_path)
    
    # Initialize Ollama chat model
    chat_model = ChatOllama(
        model="deepseek-r1:1.5b",  # Change to your preferred model (e.g., "mistral", "phi3")
        temperature=0
    )
    
    # Create QA chain
    qa_chain = RetrievalQA.from_chain_type(
        chat_model,
        retriever=db.as_retriever(search_kwargs={"k": 5}),
        chain_type="stuff"
    )
    
    return qa_chain

def main():
    st.set_page_config(page_title="Local Chatbot Q&A System", page_icon="🤖")
    st.title("📚 Local Chatbot Q&A System")
    
    # Initialize QA system
    with st.spinner("Initializing the QA system..."):
        qa_chain = initialize_qa_system()
    
    # Question input
    question = st.text_input(
        "Ask a question:",
        placeholder="Type your question here...",
        key="question_input"
    )
    
    if st.button("Get Answer", type="primary"):
        if question:
            with st.spinner("Searching for answer..."):
                try:
                    # Get answer from QA chain
                    response = qa_chain.invoke({"query": question})
                    answer = response.get("result") or response.get("answer", "No answer found.")
                    
                    st.success("Answer:")
                    st.write(answer)
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please enter a question first.")
    
    # Sidebar information
    with st.sidebar:
        st.title("ℹ️ About")
        st.markdown(""" 
        Local Q&A system powered by Ollama and LangChain.
        
        **Requirements:**
        - Ollama running locally
        - Models downloaded (e.g., `ollama pull llama2`)
        
        **How to use:**
        1. Enter your question
        2. Click 'Get Answer'
        3. View results
        """)

if __name__ == "__main__":
    main()
