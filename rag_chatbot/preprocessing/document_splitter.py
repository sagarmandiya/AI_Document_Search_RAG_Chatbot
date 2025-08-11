from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_documents(documents, chunk_size=500, overlap=50):
    splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=chunk_size, chunk_overlap=overlap
    )
    return splitter.split_documents(documents)
