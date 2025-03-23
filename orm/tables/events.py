from sqlalchemy import Column, Date, ForeignKey, Integer, String
from orm.config import Base

class Events(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    date = Column(Date)
    location = Column(String)
    create_user_id = Column(Integer, ForeignKey('users.id'))
