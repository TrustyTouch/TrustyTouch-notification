# Utiliser une image de base Python
FROM python:3.9-slim

# Installer les dépendances pour psycopg2
RUN apt-get update && apt-get install -y libpq-dev gcc

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier des dépendances et installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers du projet
COPY . .

# Exposer le port sur lequel Flask s'exécute
EXPOSE 5000

# Commande pour démarrer l'application
CMD ["flask", "run", "--host=0.0.0.0"]