
import os
import tempfile
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader

def extract_text_from_upload(uploaded_file):
    """
    Fonction utilitaire pour extraire le texte d'un fichier Streamlit (PDF, DOCX, TXT).
    Gère la création de fichier temporaire et le nettoyage.
    """
    try:
       
        file_extension = os.path.splitext(uploaded_file.name)[1].lower()
        
        
        with tempfile.NamedTemporaryFile(delete=False, suffix=file_extension) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_path = tmp_file.name

        text = ""
        
       
        if file_extension == ".pdf":
            loader = PyPDFLoader(tmp_path)
            pages = loader.load()
            text = "\n".join([p.page_content for p in pages])
            
        elif file_extension == ".docx":
            loader = Docx2txtLoader(tmp_path)
            docs = loader.load()
            text = "\n".join([d.page_content for d in docs])
            
        elif file_extension == ".txt":
            loader = TextLoader(tmp_path)
            docs = loader.load()
            text = "\n".join([d.page_content for d in docs])
            
        else:
            text = "Format non supporté. Utilisez PDF, DOCX ou TXT."

        
        os.remove(tmp_path)
        
        return text

    except Exception as e:
        return f"Erreur lors de la lecture du fichier : {str(e)}"