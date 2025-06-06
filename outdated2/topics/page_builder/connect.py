from database.query.connect import authenticate, create_user, username_exists
from topics.page_builder import PageBuilder
from topics.constants import CONNECT_MESSAGES, PAGE_NAMES, STATE_ELEMENTS

import streamlit as st


page_name=PAGE_NAMES.CONNECT.value
page_title="chEvent : Connexion | Inscription"
page_icon="🔒"

def build_func(session):
    st.header("""🔒 chEvent :""")
    st.subheader('Connexion | Inscription')
    insc, conn = st.tabs(["Inscription", "Connexion"])
    with insc :
        st.markdown("#### 🌟 Crée un nouveau compte")
        new_username = st.text_input("Nom d'utilisateur", key='champ_new_username')
        insc_feedback = st.empty()
        if st.button("S'inscrire"):
            if username_exists(session, new_username):
                insc_feedback.error("Nom d'utilisateur déjà pris.")
            else:
                code = create_user(session, new_username)
                if code:
                    insc_feedback.success(f"Compte créé avec succès ! Code de connexion : **{code}**")
                    st.balloons()
                else:
                    insc_feedback.error("Erreur lors de la création de compte.")

    with conn:
        st.markdown("#### 🔑 Connecte-toi à ton compte")
        username = st.text_input("Nom d'utilisateur", key="champ_username")
        code = st.text_input("Code de connexion", type="password")
        conn_feedback = st.empty()
        if st.button("Se connecter"):
            result = authenticate(session, username, code)
            if result == CONNECT_MESSAGES.UNKNOWN.value:
                conn_feedback.error("Utilisateur inconnu.")
            elif result == CONNECT_MESSAGES.INVALID.value:
                conn_feedback.error("Code de connection invalide.")
            else:
                st.session_state[STATE_ELEMENTS.USERNAME.value] = username
                st.session_state[STATE_ELEMENTS.PAGE_NAME.value] = PAGE_NAMES.HOME.value
                conn_feedback.success("Connexion réussie !")
                st.rerun()

connectPage = PageBuilder(
    page_name=page_name,
    page_title=page_title,
    page_icon=page_icon,
    build_func=build_func
    )
