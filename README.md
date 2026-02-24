# Recruteur Augmenté AI : Assistant RAG Local

## Description du Projet
[cite_start]Ce projet présente la conception et l'implémentation d'un assistant de recrutement intelligent basé sur l'architecture RAG (Retrieval-Augmented Generation)[cite: 5]. [cite_start]Il a été conçu pour résoudre les problématiques de surcharge cognitive et de confidentialité des données dans le processus de sélection des candidats[cite: 6]. 

[cite_start]En utilisant des modèles de langage locaux (Llama 3.2) et une base de données vectorielle [cite: 6][cite_start], ce système est capable de lire vos documents spécifiques (les CVs) avant de répondre[cite: 24].

## Problématique
[cite_start]Le processus de recrutement moderne est confronté à un défi majeur : le volume[cite: 14]. [cite_start]Un recruteur consacre en moyenne moins de 10 secondes à la lecture initiale d'un CV[cite: 15]. Cela entraîne :
* [cite_start]**La perte de talents** : Des candidats qualifiés sont rejetés par manque d'attention[cite: 17].
* [cite_start]**Les biais cognitifs** : La recherche par mots-clés ignore les nuances sémantiques[cite: 18].
* [cite_start]**Les risques de confidentialité** : L'utilisation d'IA en ligne (cloud) expose les données personnelles sensibles (PII) des candidats[cite: 20, 21].

## La Solution : RAG Local
[cite_start]Ce projet déploie une architecture RAG entièrement locale[cite: 23]. 

### Fonctionnement technique
[cite_start]Le système transforme les CVs et les offres d'emploi en vecteurs mathématiques (Embeddings)[cite: 27]. [cite_start]Cela permet de comparer le sens de l'offre d'emploi avec le sens des compétences du candidat, plutôt que de faire une simple recherche de mots[cite: 26, 28].

### Avantages stratégiques
* [cite_start]**Confidentialité totale** : Tout le traitement se fait sur la machine de l'utilisateur via Ollama, aucune donnée ne sort du réseau local[cite: 30, 31].
* [cite_start]**Gain de productivité** : Analyse croisée de dizaines de candidatures en quelques secondes[cite: 32].
* [cite_start]**Standardisation** : L'IA applique la même grille de lecture à tous les candidats, réduisant la subjectivité[cite: 33].

## Stack Technique
[cite_start]Le projet repose sur un écosystème Python robuste[cite: 43]:
* [cite_start]**Moteur d'inférence** : Ollama (Gère Llama 3.2 localement)[cite: 44].
* [cite_start]**Modèle de Langage** : Llama 3.2 (Version 1B/3B)[cite: 44].
* [cite_start]**Orchestration** : LangChain[cite: 45].
* [cite_start]**Stockage Vectoriel** : ChromaDB[cite: 45].
* [cite_start]**Interface Utilisateur** : Streamlit[cite: 46].

## Structure du Code
```text
Projet_RAG_Recrutement/
[cite_start]├── data/              # Dossier de depot des CVs (PDF) [cite: 49]
[cite_start]├── database/          # Persistance de la base vectorielle [cite: 49]
[cite_start]├── src/               # Code source [cite: 49]
[cite_start]│   ├── app.py         # Interface utilisateur (Frontend) [cite: 49]
[cite_start]│   ├── config.py      # Parametres globaux [cite: 49]
[cite_start]│   ├── database.py    # Gestion de ChromaDB [cite: 49]
[cite_start]│   ├── ingestion.py   # Traitement des PDFs (ETL) [cite: 49]
[cite_start]│   ├── rag.py         # Logique d'IA et Prompts [cite: 49]
[cite_start]│   └── utils.py       # Utilitaires (Extraction fichiers) [cite: 49]
[cite_start]└── requirements.txt   # Dependances Python [cite: 49]