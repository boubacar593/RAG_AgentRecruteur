# Recruteur Augmente AI : Assistant RAG Local

## Description du Projet
Ce projet presente la conception et l'implementation d'un assistant de recrutement intelligent base sur l'architecture RAG (Retrieval-Augmented Generation). Il a ete concu pour resoudre les problematiques de surcharge cognitive et de confidentialite des donnees dans le processus de selection des candidats. 

En utilisant des modeles de langage locaux (Llama 3.2) et une base de donnees vectorielle, ce systeme est capable de lire vos documents specifiques (les CVs) avant de repondre.

## Problematique
Le processus de recrutement moderne est confronte a un defi majeur : le volume. Un recruteur consacre en moyenne moins de 10 secondes a la lecture initiale d'un CV. Cela entraine :
* La perte de talents : Des candidats qualifies sont rejetes par manque d'attention.
* Les biais cognitifs : La recherche par mots-cles ignore les nuances semantiques.
* Les risques de confidentialite : L'utilisation d'IA en ligne (cloud) expose les donnees personnelles sensibles (PII) des candidats.

## La Solution : RAG Local
Ce projet deploie une architecture RAG entierement locale. 

### Fonctionnement technique
Le systeme transforme les CVs et les offres d'emploi en vecteurs mathematiques (Embeddings). Cela permet de comparer le sens de l'offre d'emploi avec le sens des competences du candidat, plutot que de faire une simple recherche de mots.

### Avantages strategiques
* Confidentialite totale : Tout le traitement se fait sur la machine de l'utilisateur via Ollama, aucune donnee ne sort du reseau local.
* Gain de productivite : Analyse croisee de dizaines de candidatures en quelques secondes.
* Standardisation : L'IA applique la meme grille de lecture a tous les candidats, reduisant la subjectivite.

## Stack Technique
Le projet repose sur un ecosysteme Python robuste :
* Moteur d'inference : Ollama (Gere Llama 3.2 localement).
* Modele de Langage : Llama 3.2 (Version 1B/3B).
* Orchestration : LangChain.
* Stockage Vectoriel : ChromaDB.
* Interface Utilisateur : Streamlit.

## Structure du Code
```text
Projet_RAG_Recrutement/
├── data/              # Dossier de depot des CVs (PDF)
├── database/          # Persistance de la base vectorielle
├── src/               # Code source
│   ├── app.py         # Interface utilisateur (Frontend)
│   ├── config.py      # Parametres globaux
│   ├── database.py    # Gestion de ChromaDB
│   ├── ingestion.py   # Traitement des PDFs (ETL)
│   ├── rag.py         # Logique d'IA et Prompts
│   └── utils.py       # Utilitaires (Extraction fichiers)
└── requirements.txt   # Dependances Python