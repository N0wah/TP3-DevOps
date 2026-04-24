# TP3 — Stack Hybride Docker Compose (MongoDB + MySQL + FastAPI)

## Architecture

5 services orchestrés via Docker Compose :

| Service | Image | Rôle | Port |
|---|---|---|---|
| `db_mongo` | Image custom (mongo:7.0) | Base NoSQL — stocke les articles | — |
| `db_mysql` | mysql:8.0 | Base SQL — stocke les utilisateurs | — |
| `admin_mongo` | mongo-express | Interface web MongoDB | 8081 |
| `admin_mysql` | adminer | Interface web MySQL | 8090 |
| `api` | Image custom (python:3.12-slim) | API FastAPI hybride | 8001 |

Les bases de données n'exposent aucun port — elles sont uniquement accessibles depuis les autres conteneurs.

## Structure du projet

```
TP3/
├── docker-compose.yml
├── .env.example
├── .gitignore
├── api/
│   ├── Dockerfile
│   ├── .dockerignore
│   ├── main.py
│   └── requirements.txt
├── mongo/
│   ├── Dockerfile
│   └── init-scripts/
│       └── 01_init.js
└── mysql/
    └── init-scripts/
        └── 01_init.sql
```

## Prérequis

- Docker Desktop installé et démarré

## Lancement

**1. Configurer l'environnement**

```bash
cp .env.example .env
```

Éditer `.env` et renseigner les mots de passe.

**2. Démarrer la stack**

```bash
docker compose up --build -d
```

**3. Vérifier que les 5 services sont healthy**

```bash
docker compose ps
```

Attendre que tous les services affichent `(healthy)`.

## Routes API

| Route | Source | Description |
|---|---|---|
| `GET /posts` | MongoDB | Retourne les 5 articles du blog |
| `GET /users` | MySQL | Retourne les 4 utilisateurs |
| `GET /health` | Les deux | État de santé de l'API |

```bash
curl http://localhost:8000/posts
curl http://localhost:8000/users
```

## Interfaces d'administration

- **Mongo Express** → http://localhost:8080 (login/mdp dans `.env`)
- **Adminer** → http://localhost:8080 — Système : `MySQL`, Serveur : `db_mysql`

## Arrêter la stack

```bash
# Arrêter sans supprimer les données
docker compose down

# Arrêter et supprimer les volumes (repart de zéro)
docker compose down -v
```

## Healthchecks métiers

Les healthchecks ne vérifient pas uniquement que le processus tourne, ils valident l'intégrité des données :

- **MongoDB** : vérifie que `blog_db.posts` contient exactement 5 documents
- **MySQL** : vérifie que la table `utilisateurs` contient exactement 4 lignes
- **API** : vérifie que les routes `/posts` et `/users` répondent toutes les deux
