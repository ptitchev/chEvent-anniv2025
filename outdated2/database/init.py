import datetime
import streamlit as st

from database.create import create_tables, delete_tables
from database.utils import dbUtils
from orm.table.event import Event
from orm.table.invitation import Invitation
from orm.table.user import User
from topics.constants import INVITATION_STATUS

user_me = {
    "username": "ptitchev",
    "code": st.secrets["chevpassword"],
}

event_macon = {
    "name": "TCP - vol. 3",
    "date": datetime.date(2025, 5, 30),
    "location": "Mâcon",
    'first_image_link': None,
    "description": """
        Hello le peuple !  
        Je vous propose de fêter **mon anniversaire** le zeek-end du 30 au 2 juin dans la campagne Mâconnaise.

        Au programme :

        > **Vendredi soir :** échauffement amical a base de barbecue et bière au minimum  

        > **Samedi :** ~~journée detox et sobre~~ programme libre mais perso ça sera piscine

        > **Samedi soir:** Diffusion sur vidéo-projecteur de la final de la LDC pour les intéressés, pour les autres, soirée à thème, mais je l'ai pas encore trouvé

        > **Dimanche :** pas de repos pour les guerriers, visite du troupeau de chèvre pour les intéressés
    """
}

event_paris = {
    "name": "Soirée Parisienne",
    "date": datetime.date(2025, 6, 6),
    "location": "Paris - Apérock/Supersonic",
    'first_image_link': None,
    "description": """
        Hello le peuple !  
        Je vous propose de fêter **mon anniversaire** le vendredi 6 juin 2025

        Au programme :

        > Début de soirée à **l'Apérock**, bar mythique du 17ème  
        *7 Rue Bayen, 75017 Paris*

        > Puis sortie au **Supersonic** pour les courageux

        > Et enfin potentiellement after chez moi pour les enragés
    """,
    "first_image_link": "https://github.com/ptitchev/chEvent-anniv2025/blob/main/images/paris.jpeg?raw=true",
}
events_to_create = [
    event_macon,
    event_paris,
]

invit_macon = {
    'status' : INVITATION_STATUS.ACCEPT.value
}
invit_paris = {
    'status' : INVITATION_STATUS.ACCEPT.value
}
invits_to_create = [
    invit_macon,
    invit_paris,
]

def create_if_not_exists(session, model, data):
    instance = session.query(model).filter_by(**data).first()
    if instance is None:
        instance = model(**data)
        session.add(instance)
    return instance

def init_db():
    delete_tables()
    create_tables()
    session = dbUtils.open_session()
    user = User(**user_me)
    session.add(user)
    session.flush()
    created_events = []
    for event_data in events_to_create:
        event_data = event_data.copy()
        event_data["create_user_id"] = user.id
        event = Event(**event_data)
        session.add(event)
        created_events.append(event)
    session.flush()
    invits = [
        Invitation(user_id=user.id, event_id=event.id, status=INVITATION_STATUS.ACCEPT.value)
        for event in created_events
    ]
    session.add_all(invits)
    session.commit()
