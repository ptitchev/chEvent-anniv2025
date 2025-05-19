from orm.table.chat import Message
from orm.table.user import User
from orm.table.event import Event
from orm.table.invitation import Invitation

from sqlalchemy.orm import aliased

Creator = aliased(User)
Invited = aliased(User)

def get_event_data(session, event_id, username):
    return session.query(
        Event.id,
        Event.name,
        Event.date,
        Event.location,
        Event.description,
        Creator.username.label("creator_username"),
        Invitation.id.label("invitation_id"),
        Invitation.status.label("user_status"),
    ).join(Invitation, Invitation.event_id == Event.id) \
     .join(Creator, Event.create_user_id == Creator.id) \
     .join(Invited, Invitation.user_id == Invited.id) \
     .filter(Event.id == event_id, Invited.username == username) \
     .first()

def update_invitation_status(session, invitation_id, new_user_status):
    invitation_update = (
        session.query(Invitation)
            .filter(Invitation.id == invitation_id)
            .first()
        )
    invitation_update.status = new_user_status

def get_all_invitation(session, event_id):
    return (
        session.query(
            Invitation.status.label("user_status"),
            User.username
        ).join(User, Invitation.user_id == User.id)
        .filter(Invitation.event_id == event_id)
        .all()
    )

def send_message(session, sender_username, event_id, content):
    sender = session.query(User).filter_by(username=sender_username).first()
    message = Message(sender_id=sender.id, event_id=event_id, content=content)
    session.add(message)
    session.commit()
    return True

def get_conversation(session, event_id):
    messages = (
        session.query(
            Message.id,
            Message.content,
            User.username.label("sender_username"),
            Message.timestamp,
        )
        .join(User, User.id == Message.sender_id)
        .filter(Message.event_id == event_id)
        .order_by(Message.timestamp.asc())
        .limit(250)
        .all()
    )
    return messages
