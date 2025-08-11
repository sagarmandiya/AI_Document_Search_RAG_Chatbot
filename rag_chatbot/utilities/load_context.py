import bs4
from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader

def load_from_url(url: str):
    loader = WebBaseLoader(
        web_paths=(url,),
        bs_kwargs=dict(
            parse_only=bs4.SoupStrainer(
                class_=("post-content", "post-title", "post-header")
            )
        ),
    )
    return loader.load()

def load_from_pdf(path: str):
    loader = PyPDFLoader(path)
    return loader.load()
