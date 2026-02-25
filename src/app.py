
import streamlit as st
import os
import sys


current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(root_dir)


from src.utils import extract_text_from_upload       
from src.ingestion import load_and_split_documents   
from src.database import add_documents_to_db, get_vectorstore
from src.rag import get_rag_chain


st.set_page_config(page_title="Recruteur AI", page_icon="", layout="wide")
st.title("Assistant Recrutement & Matching")


if "job_text" not in st.session_state:
    st.session_state.job_text = ""
if "messages" not in st.session_state:
    st.session_state.messages = []


with st.sidebar:
    st.header(" Base de Candidats")
    st.info("Les CVs doivent être dans le dossier 'data/'")
    
    if st.button(" Indexer les CVs (Dossier Data)"):
        with st.spinner("Indexation en cours..."):
            try:
                chunks = load_and_split_documents()
                if chunks:
                    add_documents_to_db(chunks)
                    st.success(f" {len(chunks)} fragments indexés.")
                   
                    if "rag_chain" in st.session_state:
                        del st.session_state["rag_chain"]
                else:
                    st.warning("Aucun document valide trouvé.")
            except Exception as e:
                st.error(f"Erreur technique : {e}")
    
    st.markdown("---")
    st.caption("Moteur : Llama 3.2 Local")


st.markdown("### L'Offre d'Emploi (Le Besoin)")

col_upload, col_view = st.columns([1, 2])

with col_upload:
    uploaded_job = st.file_uploader("Téléverser l'offre", type=["pdf", "docx", "txt"])
    if uploaded_job:
        with st.spinner("Lecture..."):
         
            extracted_text = extract_text_from_upload(uploaded_job)
            st.session_state.job_text = extracted_text

with col_view:
    job_description = st.text_area(
        "Contenu de l'offre (Modifiable)",
        value=st.session_state.job_text,
        height=150,
        placeholder="Le texte extrait apparaîtra ici..."
    )


if "rag_chain" not in st.session_state:
    try:
        vectorstore = get_vectorstore()
        st.session_state.rag_chain = get_rag_chain(vectorstore)
    except Exception as e:
        st.error("Erreur critique : Impossible de charger la base de données ou Ollama.")


st.markdown("### Analyse & Matching")


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("Posez votre question sur les candidats..."):
    
    if not job_description:
        st.warning("Veuillez d'abord fournir une offre d'emploi ci-dessus.")
    else:
        
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

       
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            with st.spinner("Réflexion en cours..."):
                try:
                    
                    response = st.session_state.rag_chain.invoke({
                        "input": prompt, 
                        "job_description": job_description
                    })
                    full_response = response['answer']
                    message_placeholder.markdown(full_response)
                except Exception as e:
                    message_placeholder.error(f"Erreur RAG : {e}")

       
        st.session_state.messages.append({"role": "assistant", "content": full_response})