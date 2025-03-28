### CV Extractor

cv-extractor est une API développée avec FastAPI en Python qui permet d'extraire les informations d'un CV au format PDF et de les retourner sous la forme d'un objet UserModel structuré. L'extraction est réalisée grâce à Azure OpenAI, via des requêtes HTTP à son API.

## Fonctionnalités

- Prend en entrée un fichier PDF contenant un CV.
- Analyse et extrait les informations clés du CV.
- Retourne un objet UserModel structuré avec les informations suivantes :
  - Nom et prénom
  - Email et numéro de téléphone
  - Adresse
  - Profession
  - Langues parlées
  - Formations suivies
  - Compétences
  - Expériences professionnelles

## Installation

# Prérequis

- Python 3.8+
- FastAPI
- Uvicorn
- Azure AIservices
- Postman (Pour tester l'api)

# Étapes d'installation

