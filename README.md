# SOFTDESK

Openclassrooms - Parcours développement Python Projet 10

## Status

This project is ready for evaluation.

## Description

Softdesk est une API qui permet aux utilisateurs de créer et de suivre des problèmes techniques.

Cette API est conçue pour fonctionner dans le backend d'une application iOS, Android ou Web. L'application doit permettre aux utilisateurs de créer des projets, d'ajouter des collaborateurs, de créer des problèmes et des commentaires, d'attribuer des priorités ou des balises, etc.

L'application doit utiliser les points de terminaison de l'API pour demander et écrire des données.

La documentation de l'API est disponible à l'emplacement suivant: [postman documentation](https://documenter.getpostman.com/view/20055580/UVsSLiAZ)

L'API est développée en python à l'aide de Django Rest Framework.

## Installation

Python 3 est requis pour exécuter l'API.

1. Cloner ce dépôt en utilisant `$ git clone ` (you can also download the code using [as a zip file](https://github.com/Sofiane-Mesdour/softdesk))
2. Accédez au dossier racine du référentiel
3. Créez un environnement virtuel avec`python -m venv env`
4. Activez l'environnement virtuel avec `source env/bin/activate`
5. Installer les dépendances du projet avec `pip install -r requirements.txt`
6. Lancez le serveur avec `python manage.py runserver`

## Usage

1. L'API peut être interrogée à partir de l'adresse suivante: `http://localhost:8000/api/`
2. Reportez-vous à la documentation de l'API pour la liste et la description de tous les points de terminaison: [postman documentation](https://documenter.getpostman.com/view/20055580/UVsSLiAZ)
