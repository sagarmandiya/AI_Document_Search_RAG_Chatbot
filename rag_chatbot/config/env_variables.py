import os
from dotenv import load_dotenv

load_dotenv()

DOC_SOURCE_URL = os.getenv("DOC_SOURCE_URL")
VECTOR_DB_DIR = os.getenv("VECTOR_DB_DIR", "./vector_store")
EMBED_MODEL = os.getenv("EMBED_MODEL", "all-MiniLM-L6-v2")
LLM_MODEL = os.getenv("LLM_MODEL", "sonar")