import os
import pandas as pd
import psycopg2
import streamlit as st

def rank_dataframe(df: pd.DataFrame, rank_column_name: str = "Rank") -> pd.DataFrame:
  return (
    df.reset_index(drop=True)
      .rename_axis(rank_column_name)
      .reset_index()
      .assign(**{rank_column_name: lambda x: x[rank_column_name] + 1})
  )

@st.cache_data
def load_data():
    POSTGRES_HOST = os.environ.get("POSTGRES_HOST", "postgres")
    POSTGRES_DB = os.environ.get("POSTGRES_DB", "postgres")
    POSTGRES_USER = os.environ.get("POSTGRES_USER", "airflow")
    POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "airflow")
    POSTGRES_PORT = int(os.environ.get("POSTGRES_PORT", 5432))

    conn = psycopg2.connect(
        host=POSTGRES_HOST,
        dbname=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        port=POSTGRES_PORT
    )
    query = """
        SELECT
            title AS "Title",
            author AS "Author",
            state AS "State",
            district AS "District",
            year AS "Year",
            ban_status AS "Ban Status",
            origin_of_challenge AS "Origin of Challenge"
        FROM banned_books
    """
    data = pd.read_sql(query, conn)
    conn.close()
    return data