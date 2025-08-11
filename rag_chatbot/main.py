from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from config.env_variables import *
from utilities.load_context import load_from_url
from preprocessing.document_splitter import split_documents
from preprocessing.vectorstore import create_vectorstore, load_vectorstore
from utilities.retriever import get_retriever, format_context

from langchain.prompts import ChatPromptTemplate
from langchain_perplexity import ChatPerplexity
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import os

app = FastAPI(title="RAG Chatbot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],           # Or ["http://localhost:3000"] for more security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if not os.path.exists(VECTOR_DB_DIR):
    docs = load_from_url(DOC_SOURCE_URL)
    splits = split_documents(docs)
    create_vectorstore(splits, EMBED_MODEL, VECTOR_DB_DIR)

vectorstore = load_vectorstore(EMBED_MODEL, VECTOR_DB_DIR)
retriever = get_retriever(vectorstore)

prompt = ChatPromptTemplate.from_template("""
Answer the question based only on the following context:
{context}

Question: {question}
""")
llm = ChatPerplexity(model=LLM_MODEL, temperature=0)

rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

class Query(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(query: Query):
    answer = rag_chain.invoke(query.question)
    return {"answer": answer}
