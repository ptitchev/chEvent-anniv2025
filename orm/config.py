import streamlit as st
from sqlalchemy.orm import declarative_base

Base = declarative_base()
DB_URL = st.secrets["DB_URL"]