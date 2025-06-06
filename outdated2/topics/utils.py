import streamlit as st
from database.utils import dbUtils

def st_db_health():
    DB_URI = st.secrets["DB_URI"]
    if not dbUtils.health(DB_URI):
        st.error("Site non fonctionnel : Base de donnée indisponible.")
        return False
    else:
        return True
