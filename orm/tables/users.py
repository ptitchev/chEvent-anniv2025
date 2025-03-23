from sqlalchemy import Column, Integer, String
from orm.config import Base


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)