from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine

def ingest():
    engine = create_engine('postgresql+psycopg2://user:password@db:5432/sport')
    df = pd.read_csv('/opt/airflow/dags/data/fact_resultats_epreuves.csv')
    df.to_sql('fact_resultats_epreuves', engine, if_exists='replace', index=False)

with DAG(
    dag_id='ingest_sport_data',
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,
    catchup=False
) as dag:
    task = PythonOperator(
        task_id='load_csv_to_postgres',
        python_callable=ingest
    )
