import psycopg2
import streamlit as st


def connect_db():
    connection = psycopg2.connect(st.secrets["DB_URL"])
    cursor = connection.cursor()

    return connection, cursor

def close_db(connection, cursor):
    cursor.close()
    connection.close()
