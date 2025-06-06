from sqlalchemy import Column, Integer, String
from orm.config import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    code = Column(String, nullable=False)