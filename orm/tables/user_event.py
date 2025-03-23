from sqlalchemy import Column, Integer, ForeignKey, String
from orm.config import Base

class UserEvent(Base):
    __tablename__ = 'user_event'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    event_id = Column(Integer, ForeignKey('events.id'))
    status = Column(String, nullable=False)
    message = Column(String)