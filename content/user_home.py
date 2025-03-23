import streamlit as st

from component import spawn_print_event
from orm import connect_orm, Events, Users, UserEvent
from session_state import session_user, user_event

from content.global_show import global_show

class UserHome:
    def __init__(self):
        self.name = 'user_home'
        self.is_shown = False

    def show(self):
        st.set_page_config(page_title="chEvent : Mes événements", page_icon="🎉", layout = "wide")
        global_show(self.show_int)

    def show_int(self):
        self.is_shown = True
        db_session = connect_orm()

        username = session_user.get_session_state()
        user = db_session.query(Users.id, Users.username).filter_by(username=username).first()
        user_events = (
            db_session.query(
                Events.id,
                Events.name,
                Events.date,
                Events.location,
                Events.first_image_link,
                Users.username.label("creator_username"),
                UserEvent.status.label("user_status")
            )
            .join(UserEvent, UserEvent.event_id == Events.id)
            .join(Users, Events.create_user_id == Users.id)
            .filter(UserEvent.user_id == user.id)
            .all()
        )
        db_session.close()

        st.header("""🎉 chEvent :""")
        st.markdown(f"#### Bienvenue {username} !")
        st.divider()
        st.write("A l'occasion de son 26ème anniversaire, le génial **Jules Chevenet** t'invites à différent évènements :")

        for event in user_events:
            if spawn_print_event(event, key=str(event.id)):
                user_event.update_session_state(event.id)
                st.rerun()
