from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pendulum
import pandas as pd
from sqlalchemy import create_engine

def ingest():
    engine = create_engine('postgresql+psycopg2://user:password@db:5432/sport')
    df = pd.read_csv('/opt/airflow/dags/data/fact_resultats_epreuves.csv')
    df.to_sql('fact_resultats_epreuves', engine, if_exists='replace', index=False)

local_tz = pendulum.timezone("Europe/Paris")

with DAG(
    dag_id='ingest_sport_data',
    start_date=datetime(2020, 1, 1, tzinfo=local_tz),
    schedule_interval="0 0 1 1 */4",  # Tous les 4 ans le 1er janvier à minuit
    catchup=False,
    description="DAG d'ingestion de résultats sportifs tous les 4 ans",
    tags=["sport", "ingestion"]
) as dag:
    task = PythonOperator(
        task_id='load_csv_to_postgres',
        python_callable=ingest
    )
