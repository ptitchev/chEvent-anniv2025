from sqlalchemy import create_engine
import streamlit as st

from orm.config import Base

def create_tables():
    engine = create_engine(st.secrets["DB_URI"])
    Base.metadata.create_all(engine)

def delete_tables():
    engine = create_engine(st.secrets["DB_URI"])
    Base.metadata.drop_all(engine)