from sqlalchemy import Column, Integer, String, ForeignKey
from orm.config import Base

class Invitation(Base):
    __tablename__ = "invitations"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    event_id = Column(Integer, ForeignKey('events.id'))
    status = Column(String, nullable=False)