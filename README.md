# 🤖 RAG Chatbot using Streamlit, LangChain & FAISS

A Retrieval-Augmented Generation (RAG) chatbot that allows users to upload PDF documents and ask context-aware questions. The application retrieves relevant information from the uploaded document using a FAISS vector database and generates accurate responses with an OpenAI language model.

---

## 📌 Features

* 📄 Upload PDF documents
* ✂️ Automatic text chunking
* 🧠 Generate embeddings using OpenAI Embeddings
* 🔍 Store document embeddings in FAISS
* 💬 ChatGPT-style conversational interface
* 📚 Context-aware question answering
* 📝 Persistent chat history using Streamlit Session State
* 🔄 Clear uploaded document and conversation
* ⚡ Fast and responsive Streamlit UI

---

## 🛠️ Tech Stack

* Python 3.11+
* Streamlit
* LangChain
* OpenAI
* FAISS
* PyPDF
* Python-dotenv

---

## 📂 Project Structure

```text
rag-chatbot/
│
├── app.py                 # Streamlit frontend
├── backend.py             # RAG backend
├── requirements.txt
├── .env.example
├── README.md
└── sample_rag_document.pdf
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/gayatori-san/unprof_pyai_25
cd rag-chatbot
```

### 2. Create a virtual environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API Key

Create a `.env` file from `.env.example`.

```
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Running the Application

```bash
streamlit run app.py
```

The application will open in your default web browser.

---

## 🚀 Usage

1. Launch the application.
2. Upload a PDF document using the sidebar.
3. Wait for the document to be processed and indexed.
4. Ask questions related to the uploaded document.
5. The chatbot retrieves relevant information and generates context-aware answers.

---

## 🏗️ RAG Workflow

```text
PDF Upload
     │
     ▼
Load PDF
     │
     ▼
Split into Chunks
     │
     ▼
Generate Embeddings
     │
     ▼
Store in FAISS
     │
     ▼
User Question
     │
     ▼
Similarity Search
     │
     ▼
Retrieve Relevant Chunks
     │
     ▼
Generate Answer with LLM
     │
     ▼
Display Response
```

---

## 📦 Dependencies

* streamlit
* langchain
* langchain-community
* langchain-openai
* faiss-cpu
* pypdf
* python-dotenv
* openai
* tiktoken

Install them using:

```bash
pip install -r requirements.txt
```

