# Scraper des Horaires de Cinéma

Ce projet Python basé sur Flask vise à aider les utilisateurs à trouver les horaires des films dans les cinémas proches. 
Il utilise des techniques de web scraping pour récupérer les données du site Allociné.
Les utilisateurs peuvent consulter les horaires pour la journée en cours.
La configuration des codes des cinémas est nécessaire dans le fichier `config.txt`.

## Fonctionnalités

- Récupération des horaires des films à partir du site Allociné
- Affichage des horaires pour la journée en cours
- Application web basée sur Flask

## Configuration

1. Cloner le dépôt.
2. Installer les dépendances nécessaires : `pip install -r requirements.txt`
3. Configurer les codes des cinémas :
    - Ouvrir `config.txt`
    - Ajouter les codes des cinémas souhaités en suivant le format en 5 caractères. (Se rendre sur le site de Allocine pour voir le code correspondant à votre cinéma)
    - Enregistrer le fichier

## Utilisation

1. Lancer l'application Flask : `python app.py`
2. Ouvrir un navigateur web et accéder à `http://localhost:5000`
3. Consulter les horaires des films pour les cinémas configurés dans `config.txt`

## Prérequis

- Python 3.x
- Flask
- Beautiful Soup (pour le web scraping)

## Avertissement

Ce projet est à des fins éducatives uniquement. Utilisez-le de manière responsable et respectez les conditions d'utilisation du site Allociné.
