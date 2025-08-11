from langchain_community.vectorstores import Chroma
from .embeddings import get_embedder

def create_vectorstore(documents, embed_model: str, persist_dir: str):
    embeddings = get_embedder(embed_model)
    vectorstore = Chroma.from_documents(documents=documents, embedding=embeddings, persist_directory=persist_dir)
    vectorstore.persist()
    return vectorstore

def load_vectorstore(embed_model: str, persist_dir: str):
    embeddings = get_embedder(embed_model)
    return Chroma(persist_directory=persist_dir, embedding_function=embeddings)
