import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.set_page_config(page_title="Analyse Sportive", layout="wide")
st.title("Explorateur de Résultats Sportifs")

def get_engine():
    return create_engine("postgresql+psycopg2://user:password@db:5432/sport")

query = st.text_area("Entre ta requête SQL :", "SELECT * FROM fact_resultats_epreuves LIMIT 10")

if st.button("Exécuter"):
    try:
        engine = get_engine()
        df = pd.read_sql_query(query, engine)
        st.dataframe(df)
    except Exception as e:
        st.error(f"Erreur : {e}")
