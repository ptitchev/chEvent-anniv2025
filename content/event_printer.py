import requests
import streamlit as st
from PIL import Image
from io import BytesIO

from orm import connect_orm, Events, Users, UserEvent
from session_state import session_user, user_event

from content.global_show import global_show

class EventPrinter:
    def __init__(self):
        self.name = 'event_printer'
        self.is_shown = False
    
    def show(self):
        st.set_page_config(page_title="chEvent : Mes événements", page_icon="🎉", layout = "wide")
        global_show(self.show_int)

    def show_int(self):
        self.is_shown = True
        db_session = connect_orm()

        username = session_user.get_session_state()
        user = db_session.query(Users.id, Users.username).filter_by(username=username).first()
        
        event_id = user_event.get_session_state()
        user_event_show = (
            db_session.query(
                Events.id,
                Events.name,
                Events.date,
                Events.location,
                Users.username.label("creator_username"),
                UserEvent.id.label('user_event_id'),
                UserEvent.status.label("user_status"),
                UserEvent.message.label("user_message"),
            )
            .join(UserEvent, UserEvent.event_id == Events.id)
            .join(Users, Events.create_user_id == Users.id)
            .filter(UserEvent.user_id == user.id, Events.id == event_id)
            .first()
        )


        st.header(user_event_show.name)
        st.divider()
        st.write(f'📍 {user_event_show.location}')
        st.write(f'📅 {user_event_show.date.strftime("%d %B %Y")}')
        st.write(f'👤 {user_event_show.creator_username}')
        st.markdown(f"""<strong style="color: {'#4CAF50' if user_event_show.user_status == 'Accepté' else '#F44336' if user_event_show.user_status == 'Refusé' else '#FF9800' if user_event_show.user_status == "Attente de réponse" else '#000000'}">
                            {user_event_show.user_status}
                        </strong>""", unsafe_allow_html=True )
        st.divider()
        invit, event = st.tabs(["Mon invitation", "Événement"])

        status_colors = {
            "Accepté": "#4CAF50",
            "Attente de réponse": "#FF9800",
            "Refusé": "#F44336",
        }
        
        possible_status = list(status_colors.keys())
        styled_options = [
            f"<span style='color: {status_colors[status]}; font-weight: bold;'>{status}</span>"
            for status in possible_status
        ]
        user_status_index = possible_status.index(user_event_show.user_status)
        with invit:
            with st.form('invit_event', border=False):
                user_event_status_change = st.radio(
                    label="Ton choix",
                    options=possible_status,
                    index=user_status_index,
                    horizontal=True
                )
                invit_message = st.text_area(
                    label="Ptit message pour Jules",
                    value=user_event_show.user_message,
                    max_chars=255,
                )
                validate_modification = st.form_submit_button("Valider")

                if validate_modification:
                    user_event_update = (
                        db_session.query(UserEvent)
                            .filter(UserEvent.id == user_event_show.user_event_id)
                            .first()
                        )
                    
                    if user_event_update:
                        user_event_update.status = user_event_status_change
                        user_event_update.message = invit_message
                        db_session.commit()

                        st.success("Réponse enregistrée avec succès 🎉")
                        st.rerun()
                    else:
                        st.error("Erreur lors de la mise à jour 🚨")

        with event:
            description = """
                Hello le peuple !  
                Je vous propose de fêter **mon anniversaire** le vendredi 4 juin 2025

                Au programme :

                > Début de soirée à **l'Apérock**, bar mythique du 17ème  
                *7 Rue Bayen, 75017 Paris*

                > Puis sortie au **Supersonic** pour les courageux

                > Et enfin potentiellement after chez moi pour les enragés
                """
            st.markdown(description)
            with st.expander(label='Invités'):
                all_users_event = (
                    db_session.query(
                    UserEvent.status.label("user_status"),
                    UserEvent.message.label("user_message"),
                    Users.username,
                )
                .join(Users, UserEvent.user_id == Users.id)
                .filter(UserEvent.event_id == event_id)
                .all()
                )
                db_session.close()

                status_filter = st.segmented_control("Filtre", possible_status, selection_mode='multi', key="filtre")
                if len(status_filter) > 0:
                    filtered_users = [
                        user
                        for user in all_users_event
                        if user.user_status in status_filter
                    ]
                else:
                    filtered_users =  all_users_event

                order_status = possible_status + ['Organisateur']
                filtered_users.sort(
                    key=lambda user: order_status.index(user.user_status)
                )

                for user in filtered_users:
                    st.markdown(
                    f"""
                    <div style="border: 1px solid #ddd; padding: 10px; border-radius: 10px; margin-bottom: 10px; background-color: #f9f9f9;">
                        <strong>👤 {user.username}</strong>  
                        <span style="color: {'#4CAF50' if user.user_status == 'Accepté' else '#F44336' if user.user_status == 'Refusé' else '#FF9800' if user.user_status == "Attente de réponse" else '#000000'}">
                            - {user.user_status}
                        </span>  
                        <p style="font-style: italic;">📩 {user.user_message if user.user_message else "Pas de message laissé."}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                    
            select_archive_menu = st.expander('Voir les archives')
            archives = [
                {'name': "The Chev Party - volume 1", "date": "Juin 2023", "logo": 'https://raw.githubusercontent.com/ptitchev/private_streamlit/main/source/logo.png', "link":'https://projet-chev.streamlit.app/TCP1'},
                {'name': "The Chev Party - volume 2", "date": "Juin 2024", "logo": 'https://raw.githubusercontent.com/ptitchev/private_streamlit/main/source/logo2.png', "link":'https://projet-chev.streamlit.app'}
            ]
            with select_archive_menu :
                c1, c2 = st.columns(2)
                with c1 :
                    archive = archives[0]
                    response = requests.get(url = archive['logo'])
                    image = Image.open(BytesIO(response.content))
                    st.image(image, caption=archive["date"])
                    st.link_button('Accéder', archive['link'], use_container_width=True)
                with c2 :
                    archive = archives[1]
                    response = requests.get(url = archive['logo'])
                    image = Image.open(BytesIO(response.content))
                    st.image(image, caption=archive["date"])
                    st.link_button('Accéder', archive['link'], use_container_width=True)      
        st.markdown(
            """
            <style>

            .stFormSubmitButton>button {
                border-radius: 10px;
                padding: 8px 20px;
                transition: 0.3s;
                width: 200px;
                margin: auto;
                display: block;

            .stFormSubmitButton>button:hover{
                color: grey;

            .st-key-filtre {
                width: 100%;
                display: flex;
                justify-content: space-around;
            }
            

            }
            """,
            unsafe_allow_html=True,
        )