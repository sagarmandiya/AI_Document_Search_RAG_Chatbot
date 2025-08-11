def get_retriever(vectorstore, k=3):
    return vectorstore.as_retriever(search_kwargs={"k": k})

def format_context(docs):
    return "\n\n".join(doc.page_content for doc in docs)
