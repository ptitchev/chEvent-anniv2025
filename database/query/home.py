from orm.table.user import User
from orm.table.event import Event
from orm.table.invitation import Invitation

from sqlalchemy.orm import aliased

Creator = aliased(User)
Invited = aliased(User)

def get_user_invitations(session, username):
    return session.query(
        Event.id,
        Event.name,
        Event.date,
        Event.location,
        Event.first_image_link,
        Creator.username.label("creator_username"),
        Invitation.status.label("user_status")
    ).join(Invitation, Invitation.event_id == Event.id) \
     .join(Creator, Event.create_user_id == Creator.id) \
     .join(Invited, Invitation.user_id == Invited.id) \
     .filter(Invited.username == username) \
     .order_by(Event.date) \
     .all()