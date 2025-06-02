# Explorateur de Résultats Sportifs

Ce projet propose une application d'analyse de données sportives combinant **Apache Airflow**, **PostgreSQL** et **Streamlit**, orchestrée via **Docker Compose**. Il permet de simuler l’arrivée de nouvelles données tous les 4 ans, de les injecter dans une base PostgreSQL, puis de les explorer via une interface web.

---

## Sommaire

- [Objectifs](#objectifs)
- [Architecture technique](#architecture-technique)
- [Fonctionnement](#fonctionnement)
- [Structure du projet](#structure-du-projet)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Technologies utilisées](#technologies-utilisées)

---

## Objectifs

- Automatiser le traitement et le chargement de résultats sportifs via Apache Airflow.
- Visualiser dynamiquement les données via une interface Streamlit connectée à PostgreSQL.
- Simuler une ingestion périodique (tous les 4 ans) comme dans le cadre de Jeux Olympiques.

---

## Architecture technique

```
Utilisateur
   │
   ├── Accès Streamlit (port 8501 - Requêtage de la base de données)
   │
   └── Accès Airflow (port 8080 - Gestion des DAGs)

Docker Compose
   ├── PostgreSQL (db)
   │
   ├── Streamlit App (app - Interface graphique)
   │
   ├── Airflow Webserver (airflow - Interface de gestion de pipelines)
   │
   └── Airflow Init (airflow-init - Init. Airflow et création de l’utilisateur)
```

---

## Fonctionnement

### 1. **Initialisation**

- La base PostgreSQL est initialisée avec un schéma via `init.sql`.
- Airflow est configuré avec un utilisateur `admin`.

### 2. **Pipelines Airflow**

Deux DAGs sont définis :

- `ingest_sport_data`: Charge une première fois les résultats depuis le fichier CSV vers PostgreSQL.
- `inject_new_sport_data`: Simule l’arrivée de nouveaux résultats tous les 4 ans (`schedule_interval="*/4 * * *"` ou déclenchement manuel).

Chaque DAG lit un fichier `.csv`, puis les insère dans la table `fact_resultats_epreuves`.

### 3. **Application Streamlit**

Accessible sur `localhost:8501`, elle permet :

- D’exécuter des requêtes SQL libres sur la base.
- D’afficher dynamiquement les résultats dans un tableau.

---

## Structure du projet

```
APP_ANALYSE_DONNEES_SPORTIVES/
│
├── app/
│   ├── main.py   
│   └── Dockerfile  
│
├── airflow/
│   ├── dags/
│   │   ├── ingest_data.py   
│   │   └── data/
│   │       └── fact_resultats_epreuves.csv
│   ├── requirements.txt  
│   └── Dockerfile      
│
├── database/
│   └── init.sql          
├── docker-compose.yml     
└── README.md
```

---

## Installation

### Prérequis

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Étapes

1. Cloner le dépôt :

   ```bash
   git clone https://github.com/Mohamedi-Ahmed/app_analyse_donnees_sportives.git
   cd APP_ANALYSE_DONNEES_SPORTIVES
   ```
2. Lancer les services :

   ```bash
   docker-compose up --build
   ```
3. Accéder à :

   - Airflow : [http://localhost:8080](http://localhost:8080) (admin/admin)
   - Streamlit : [http://localhost:8501](http://localhost:8501)

---

## Utilisation

1. Dans Airflow :

   - Dépauser les DAGs.
   - Lancer `ingest_sport_data` pour charger les premières données.
   - Planifier ou déclencher manuellement `inject_new_sport_data`.
2. Dans Streamlit :

   - Entrer une requête SQL (ex : `SELECT * FROM fact_resultats_epreuves LIMIT 10`)
   - Visualiser les résultats.

---

## Technologies utilisées

- Python 3.11
- Streamlit
- Apache Airflow 2.7.3
- PostgreSQL 15
- Docker / Docker Compose
- Pandas, SQLAlchemy, psycopg2
