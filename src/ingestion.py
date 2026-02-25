
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.config import DATA_PATH, CHUNK_SIZE, CHUNK_OVERLAP

def load_and_split_documents():
    print(f"Chargement des CVs depuis {DATA_PATH}...")
    
   
    loader = DirectoryLoader(DATA_PATH, glob="*.pdf", loader_cls=PyPDFLoader)
    raw_documents = loader.load()
    print(f" {len(raw_documents)} pages de CVs chargées.")

   
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    chunks = text_splitter.split_documents(raw_documents)
    print(f"Découpage terminé : {len(chunks)} morceaux créés.")
    
    return chunks