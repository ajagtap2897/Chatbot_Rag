# Chatbot_Rag

 **Project Overview**  
This project implements a **Retrieval-Augmented Generation (RAG) chatbot** that combines **retrieval-based search** with **generative AI** for context-aware responses. It leverages **pretrained language models (LLMs)** along with retrieval techniques to fetch relevant information before generating intelligent replies.  

---

## 🚀 **Features**  
✅ **Retrieval-Augmented Generation (RAG)** for more accurate and context-aware responses  
✅ Integrates **pretrained large language models (LLMs)** for intelligent chatbot interactions  
✅ Uses **Ollama** for running LLMs efficiently  
✅ Supports **Streamlit UI** for an interactive web-based chatbot experience  
✅ Easily customizable for **domain-specific knowledge**  

---

## 🛠 **Installation**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/ajagtap2897/Chatbot_Rag.git
cd Chatbot_Rag
```

### 2️⃣Install Ollama
This chatbot requires Ollama, a tool for running and managing LLMs locally.

### 3️⃣ Download Required Models
After installing Ollama, run the following commands to download the required models:

```bash
ollama pull nomic-embed-text:latest
ollama pull deepseek-r1:1.5b
```

### 4️⃣ Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv chatbot_env
source chatbot_env/bin/activate  # On macOS/Linux
chatbot_env\Scripts\activate     # On Windows
```

### 5️⃣ Install Dependencies:

```bash
pip install -r requirements.txt
```

## 🎯 Usage

### 1️⃣ Running the Chatbot
Start the chatbot UI using Streamlit:

```bash
streamlit run main1.py
```
This will launch an interactive web UI where users can enter queries and receive intelligent responses.

![image_alt](https://github.com/ajagtap2897/Chatbot_Rag/blob/5040204422028df56cfed901db3708c6452fb79e/Screenshot%202025-03-12%20211849.png)

### 2️⃣ Customizing the Chatbot:

Modify the retrieval pipeline to fetch data from external sources like databases, PDFs, or APIs.
Ensure the LLM integration is configured properly for your use case.


## 🔧 Customization Options

LLM Model: Replace the deepseek-r1:1.5b model with any other Ollama-compatible LLM.
Data Sources: Extend the retrieval system to pull information from research papers, enterprise databases, or knowledge bases.
Fine-Tuning: You can fine-tune the chatbot for domain-specific applications.

## 📌 Key Technologies Used
🔹 Python
🔹 Streamlit (UI)
🔹 Retrieval-Augmented Generation (RAG)
🔹 Ollama for LLM execution
🔹 Large Language Models (LLMs)

## ⚡ Future Enhancements
🚀 Add support for multi-document retrieval
🚀 Integrate vector databases for efficient knowledge retrieval
🚀 Enhance chatbot with voice input/output

## 💡 Note: This chatbot framework can be adapted for any AI-powered assistant by modifying the retrieval pipeline and model integration. 🎯
