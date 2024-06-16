# Anime List Web Application

Cette application est un projet basé sur Python qui récupère les 50 meilleurs animes de MyAnimeList en utilisant leur API, stocke les données dans une base de données SQLite, et affiche les informations dans une application web en utilisant Flask.

## Caractéristiques

- Récupère les données de l'API MyAnimeList.
- Stocke les données récupérées dans une base de données SQLite.
- Affiche les données d'anime dans une application web.

## Fichiers

- `utile/fetch_api.py`: Contient la fonction pour récupérer les 50 meilleurs animes de MyAnimeList.
- `database/script_db.py`: Contient la fonction pour récupérer les données d'anime et les stocker dans la base de données.
- `utile/data.py`: Contient des fonctions pour stocker les données d'anime récupérées dans la base de données SQLite et récupérer les données stockées de la base de données.
- `app.py`: Contient la fonction principale qui récupère les données d'anime de la base de données et les affiche dans l'application web.
- `templates/index.html`: Contient le code HTML pour l'interface utilisateur de l'application web.
- `static/css/index.css`: Contient le code CSS pour le style de l'application web.

## Comment exécuter

1. Assurez-vous d'avoir Python installé sur votre système.
2. Clonez le dépôt sur votre machine locale.
3. Naviguez vers le répertoire du projet dans votre terminal.
4. Installez les dépendances nécessaires avec la commande `pip install -r requirements.txt`.
5. Exécutez le fichier `app.py` en utilisant la commande `python app.py`.
6. Ouvrez votre navigateur web et accédez à `http://localhost:5000`.

## Dépendances

- Python
- Flask
- requests
- sqlite3
- http.client
- json

## Note

Ce projet est à des fins éducatives uniquement. La clé API MyAnimeList utilisée dans ce projet est un placeholder et ne fonctionnera pas. Veuillez la remplacer par votre propre clé API pour récupérer les données de MyAnimeList.