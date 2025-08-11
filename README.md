# 🧠 AI Document Search (RAG Chatbot)

A **Retrieval-Augmented Generation (RAG)** chatbot that lets you search and query documents (web pages, PDFs, etc.) using a Natural Language interface — built with **FastAPI + LangChain (backend)** and **React + TypeScript (frontend)**.

---

## 📂 Project Structure

AI_Document_Search_RAG_Chatbot/  
│  
├── rag_chatbot/ # Backend (FastAPI + LangChain + Chroma)  
│ ├── config/ # Configuration & env variables  
│ ├── preprocessing/ # Chunking, embeddings, vector store creation  
│ ├── utilities/ # Document loaders & retrievers  
│ ├── main.py # FastAPI app entrypoint  
│ ├── requirements.txt  
│ ├── README.md (optional backend-specific)  
│  
├── rag-chatbot-frontend/ # Frontend (React + TypeScript)  
│ ├── src/api/ # API client  
│ ├── src/components/ # UI Components (Chat UI)  
│ ├── public/  
│ ├── package.json  
│ ├── tsconfig.json  
│ ├── README.md (optional frontend-specific)  
│  
└── .env.example # Template env file  

  
---

## ⚙️ Features

- **Document Loading:** Load from URLs or PDF files.
- **Preprocessing:** Text chunking & token-aware splitting.
- **Vector Search:** Embed & store in Chroma vector DB.
- **LLM Integration:** Works with Perplexity.ai API (Sonar model) or OpenAI.
- **Frontend UI:** Simple chat interface to query your document.
- **MLOps Ready:** Modular structure, `.env` config, API-key safety, vector DB persistence.

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
[git clone https://github.com/sagarmandiya/AI_Document_Search_RAG_Chatbot.git](https://github.com/sagarmandiya/AI_Document_Search_RAG_Chatbot.git)

`cd "AI_Document_Search_RAG_Chatbot"`


---

## 🔹 Backend Setup (FastAPI + LangChain)

### Prerequisites
- Python 3.10+ and `pip`
- `virtualenv` (optional but recommended)

### Install dependencies
```cd rag_chatbot  
python -m venv .venv  
source .venv/bin/activate # Windows: .venv\Scripts\activate  
pip install -r requirements.txt  
```


### Environment Variables

Create a `.env` in `rag_chatbot/`:  
```
# Document source to index

DOC_SOURCE_URL=https://lilianweng.github.io/posts/2023-06-23-agent/

# Vector DB location

VECTOR_DB_DIR=./vector_store

# Models

EMBED_MODEL=all-MiniLM-L6-v2
LLM_MODEL=sonar

# LangChain API tracing (optional)

LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_API_KEY=your-langchain-api-key

# Perplexity API Key

PPLX_API_KEY=your-perplexity-api-key
```


> ⚠️ Do **NOT** commit `.env` to GitHub — keep it in `.gitignore`.


### Run the Backend

```
uvicorn main:app --reload
```

Server runs at: [**http://127.0.0.1:8000**](http://127.0.0.1:8000)

---

## 🔹 Frontend Setup (React + TypeScript)

### Install Dependencies

```
cd ../rag-chatbot-frontend  
npm install
```


### API Configuration

Edit `src/api/chatbot.ts` to point to your backend URL:
```
const API_BASE_URL = "http://127.0.0.1:8000";
```

If backend runs locally, you can also add in `package.json`:
```
"proxy": "http://127.0.0.1:8000"
```



### Run Frontend

```
npm start
```

Frontend runs at: [**http://localhost:3000**](http://localhost:3000)

---

## 📡 Example Usage

Once both frontend and backend are running:
1. Open [**http://localhost:3000**](http://localhost:3000) in your browser
2. Type: `What is Task Decomposition?`
3. Bot responds with context‑aware answer from the indexed document(s)

---

## 🛠 MLOps & Deployment Notes

- **Persistence:** Vector DB stored locally in `vector_store/`. Deploy to cloud storage for production.
- **Keys:** Store API keys in environment variables — never commit to GitHub.
- **Monitoring:** Integrate logging / tracing via LangChain's tracing API.
- **Scaling:** Deploy backend to services like **Render, AWS Lambda, Azure Functions** and frontend to **Netlify/Vercel**.
- **Testing:** Add `pytest` for backend and React Testing Library/Jest for frontend.

---

## 📦 Requirements

### Backend (`rag_chatbot/requirements.txt`)

```
langchain
langchain-community
langchain-core
bs4
pypdf
sentence-transformers
chromadb
fastapi
uvicorn
python-dotenv
```


### Frontend (`rag-chatbot-frontend/package.json` - dependencies excerpt)

```
"dependencies": {
"axios": "^latest",
"react": "^18.x",
"react-dom": "^18.x",
"typescript": "^5.x",
"@types/react": "^18.x",
"@types/react-dom": "^18.x"
}
```


---

## 📜 License
This project is licensed under the MIT License — see the LICENSE file for details.

---

## 🙌 Acknowledgements
- [LangChain](https://www.langchain.com/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [React](https://react.dev/)
- [Chroma](https://www.trychroma.com/)
- [Perplexity](https://www.perplexity.ai/)
