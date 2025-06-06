from custom_component.archive.component import spawn_archive
from custom_component.event_printer.component import spawn_print_event
from database.query.home import get_user_invitations
from topics.constants import PAGE_NAMES, STATE_ELEMENTS
from topics.page_builder import PageBuilder

import streamlit as st

page_name=PAGE_NAMES.HOME.value
page_title="chEvent : Mes événements"
page_icon="🎉"

def build_func(session):
    username = st.session_state[STATE_ELEMENTS.USERNAME.value]
    user_invitations = get_user_invitations(session, username)
    st.balloons()
    st.header("""🎉 chEvent :""")
    st.markdown(f"#### Bienvenue {username} !")

    even, prof = st.tabs(["Mes évenements", "Mon profil"])

    with even:
        st.write("A l'occasion de son 26ème anniversaire, le génial **Jules Chevenet** t'invites à différent évènements :")
        for event in user_invitations:
            if spawn_print_event(event, key=str(event.id)):
                st.session_state[STATE_ELEMENTS.EVENT_ID.value] = event.id
                st.session_state[STATE_ELEMENTS.PAGE_NAME.value] = PAGE_NAMES.EVENT.value
                #is_organisator.update_session_state(event.user_status == INVITATION_STATUS.ORGANISATOR.value)
                st.rerun()
        
    with prof:
        st.write(f"👤 Nom d'utilisateur : **{username}**")
        st.warning("En cours de construction")

    spawn_archive()

homePage = PageBuilder(
    page_name=page_name,
    page_title=page_title,
    page_icon=page_icon,
    build_func=build_func
    )