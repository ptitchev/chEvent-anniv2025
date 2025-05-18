import random

from sqlalchemy.exc import IntegrityError
from orm.table.invitation import Invitation
from orm.table.user import User
from orm.table.event import Event
from topics.constants import CONNECT_MESSAGES, INVITATION_STATUS

import streamlit as st


def username_exists(session, username):
    return session.query(User).filter_by(username=username).first() is not None

def create_user(session, username):
    code = f"{random.randint(1000, 9999)}"
    user = User(username=username, code=code)
    try:
        session.add(user)
        session.flush()
        events = session.query(Event.id).filter(Event.name.in_([
            "TCP - vol. 3",
            "Soirée Parisienne",
        ])).all()
        invitations = [
            Invitation(user_id=user.id, event_id=event_id, status=INVITATION_STATUS.WAITING.value)
            for (event_id,) in events
        ]
        session.add_all(invitations)
        session.commit()
        return code
    
    except IntegrityError:
        session.rollback()
        return None

def authenticate(session, username, code):
    user = session.query(User).filter_by(username=username).first()
    if not user:
        return CONNECT_MESSAGES.UNKNOWN.value
    if user.code != code:
        return CONNECT_MESSAGES.INVALID.value
    return CONNECT_MESSAGES.SUCCESS.value
