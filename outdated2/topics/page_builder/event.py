import streamlit as st

from custom_component.archive.component import spawn_archive
from custom_component.status_displayer.component import spawn_guests_status_filter, spawn_status_displayer, spawn_status_changer
from database.query.event import get_conversation, get_event_data, send_message, update_invitation_status, get_all_invitation
from topics.constants import PAGE_NAMES, STATE_ELEMENTS
from topics.page_builder import PageBuilder

page_name=PAGE_NAMES.EVENT.value
page_title="chEvent : Mes événements"
page_icon="🎉"

def build_func(session):
    username = st.session_state[STATE_ELEMENTS.USERNAME.value]
    event_id = st.session_state[STATE_ELEMENTS.EVENT_ID.value]
    invitation = get_event_data(session, event_id, username)
    guests = get_all_invitation(session, event_id)
    st.header(invitation.name)
    st.divider()
    st.write(f'📍 {invitation.location}')
    st.write(f'📅 {invitation.date.strftime("%d %B %Y")}')
    st.write(f'👤 {invitation.creator_username}')
    spawn_status_displayer(invitation.user_status)
    st.write("")
    invi, even, chat = st.tabs(["Mon invitation", "Événement", "Discussion"])

    with invi:
        with st.form('invit_event', border=False):
            change_status = spawn_status_changer(invitation.user_status)
            validate_modification = st.form_submit_button("Valider")
            changed = change_status != invitation.user_status
            if validate_modification and changed:
                update_invitation_status(session, invitation.invitation_id, change_status)
                session.commit()
                st.rerun()
        st.divider()
        st.write('**Liste des invités**')
        spawn_guests_status_filter(guests)

    with even:
        st.markdown(invitation.description)

    with chat:
        messages = get_conversation(session, event_id)
        min_height = min(len(messages) * 120, 600)
        with st.container(height=min_height):
            for message in messages:
                with st.chat_message("user"):
                    st.write(f"**{message.sender_username}**")
                    st.write(message.content)

        prompt = st.chat_input("Envoi ton message aux autres", max_chars=100)
        if prompt:
            send_message(session, username, event_id, prompt)
            st.rerun()

    st.divider()
    back_home = st.button("Retour à mon espace utilisateur")
    if back_home:
        st.session_state[STATE_ELEMENTS.EVENT_ID.value] = None
        st.session_state[STATE_ELEMENTS.PAGE_NAME.value] = PAGE_NAMES.HOME.value
        st.rerun()

    spawn_archive()

eventPage = PageBuilder(
    page_name=page_name,
    page_title=page_title,
    page_icon=page_icon,
    build_func=build_func
    )
