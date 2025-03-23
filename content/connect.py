import streamlit as st
import bcrypt

from orm.tables.events import Events
from orm.tables.user_event import UserEvent
from session_state import session_user
from orm import connect_orm, Users

from content.global_show import global_show


class Connect:
    def __init__(self):
        self.name = "connect"
        self.is_shown = False

    def hash_password(self, password):
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    def check_password(self, password, hashed):
        return bcrypt.checkpw(password.encode("utf-8"), hashed.encode("utf-8"))
    
    def try_connect(self, db_session, with_mail, mail, username, password):
        if with_mail:
            if mail == "":
                st.error("Renseigne un mail")
                return
            else:
                user = db_session.query(Users).filter_by(email=mail).first()
        else:
            if username == "":
                st.error("Renseigne un nom d'utilisateur")
                return
            user = db_session.query(Users).filter_by(username=username).first()

        if user is not None and self.check_password(password, user.password_hash):
            session_user.update_session_state(user.username)
            st.rerun()
            
        else:
            if with_mail:
                st.error("Email ou mot de passe incorrect")
            else:
                st.error("Nom d'utilisateur ou mot de passe incorrect")

        
    def try_sub(self, db_session, new_username, new_mail, new_password):
        if db_session.query(Users).filter_by(email=new_mail).first() and new_mail != "":
            st.error("Ce mail est déjà utilisé")
        elif db_session.query(Users).filter_by(username=new_username).first():
            st.error("Ce nom d'utilisateur est déjà utilisé")
        elif new_username == None or new_username == "":
            st.error("Renseigne un nom d'utilisateur")
        else:
            hashed_pw = self.hash_password(new_password)
            new_user = Users(email=new_mail, username=new_username, password_hash=hashed_pw)
            db_session.add(new_user)
            db_session.flush()
            for event_name in ["Soirée parisienne", "TCP - vol. 3"]:
                event_id = db_session.query(Events.id).filter_by(name=event_name).scalar()
                if event_id:
                    if event_name == "Soirée parisienne":
                        status = "Attente de réponse"
                    else :
                        status = "Bloqué"
                    db_session.add(UserEvent(user_id=new_user.id, event_id=event_id, status=status))
            db_session.commit()
            st.balloons()
            st.success("Inscription réussie! Connecte-toi maintenant.")
            
    def show(self):
        st.set_page_config(page_title="chEvent : Connexion | Inscription", page_icon="🔒", layout = "wide")
        global_show(self.show_int)

    def show_int(self):
        self.is_shown = True
        db_session = connect_orm()

        st.header("""🔒 chEvent :""")
        st.subheader('Connexion | Inscription')

        tab1, tab2 = st.tabs(["Connexion", "Inscription"])

        with tab1:
            st.markdown("#### 🔑 Connecte-toi à ton compte")
            with_mail = st.toggle("Utiliser le mail")
            if with_mail:
                mail = st.text_input("Mail", key='champ_mail')
                username = None
            else:
                username = st.text_input("Nom d'utilisateur", key="champ_user")
                mail = None
            password = st.text_input("Mot de passe", type="password", key='champ_password')

            if st.button("Se connecter"):
                self.try_connect(db_session, with_mail, mail, username, password)


        with tab2:
            st.markdown("#### 🌟 Crée un nouveau compte")
            new_username = st.text_input("Nom d'utilisateur", key='champ_new_user')
            new_mail = st.text_input("Mail", key='new_mail')
            new_password = st.text_input("Mot de passe", type="password", key='champ_new_password')

            if st.button("S'inscrire"):
                 self.try_sub(db_session, new_username, new_mail, new_password)

        st.markdown(
            """
            <style>

            .stTextInput>div>div>input {
                border-radius: 10px;
                padding: 10px;
                border: 1px solid #ddd;
            }

            .stButton>button {
                border-radius: 10px;
                padding: 8px 20px;
                transition: 0.3s;
                width: 200px;
                margin: auto;
                display: block;
            }

            .block-container {
                max-width: 500px;
                margin: auto;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

                