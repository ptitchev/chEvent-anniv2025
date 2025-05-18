import streamlit as st

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

class dbUtils :

    def health(db_uri: str) -> bool:
        try:
            engine = create_engine(db_uri, connect_args={"connect_timeout": 5})
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            return True

        except Exception as e:
            return False
        
    def open_session():
        engine = create_engine(st.secrets["DB_URI"])
        Session = sessionmaker(bind=engine)
        session = Session()
        return session