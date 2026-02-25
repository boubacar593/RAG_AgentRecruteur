
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from src.config import DB_PATH, EMBEDDING_MODEL


def get_embedding_function():
    return OllamaEmbeddings(model=EMBEDDING_MODEL)


def get_vectorstore():
    embedding_function = get_embedding_function()
    

    vectorstore = Chroma(
        persist_directory=DB_PATH,
        embedding_function=embedding_function
    )
    return vectorstore


def add_documents_to_db(chunks):
    db = get_vectorstore()
    print("Sauvegarde des vecteurs dans ChromaDB...")
    db.add_documents(chunks)
   
    print("Base de données mise à jour !")