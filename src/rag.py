from langchain_ollama import ChatOllama
from src.config import MODEL_NAME

class SimpleRAG:
    def __init__(self, vectorstore):
        self.vectorstore = vectorstore
        self.llm = ChatOllama(model=MODEL_NAME)

    def invoke(self, inputs):
        
        question = inputs["input"]
        job_desc = inputs.get("job_description", "Aucune fiche de poste fournie.")
        
       
        search_query = f"{question} {job_desc}"
        docs = self.vectorstore.similarity_search(search_query, k=4)
        
       
        context_text = "\n\n---\n\n".join([doc.page_content for doc in docs])
        if not context_text:
            context_text = "Aucune information trouvée dans les documents."

      
        prompt = f"""
        Tu es un Assistant Recrutement Expert. Ton but est de trouver le meilleur "Fit" (correspondance).
        
        SOURCE 1 : LA FICHE DE POSTE (CE QU'ON CHERCHE)
        "{job_desc}"
        
        SOURCE 2 : LES PROFILS TROUVÉS (CE QU'ON A)
        {context_text}
        
        TA MISSION :
        Réponds à la question de l'utilisateur en comparant strictement les Profils avec la Fiche de Poste.
        - Si un candidat a une compétence demandée, dis-le.
        - Si un candidat MANQUE d'une compétence clé de la fiche de poste, signale-le comme un risque.
        - Sois factuel. Cite les expériences.
        
        QUESTION DE L'UTILISATEUR :
        "{question}"
        """

       
        print("Analyse croisée Poste <-> Candidats en cours...")
        response = self.llm.invoke(prompt)
        
        return {"answer": response.content}

def get_rag_chain(vectorstore):
    return SimpleRAG(vectorstore)