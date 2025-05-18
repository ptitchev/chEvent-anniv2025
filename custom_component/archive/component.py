import requests
import streamlit as st
from PIL import Image
from io import BytesIO

archives = [
    {'name': "The Chev Party - volume 1", "date": "Juin 2023", "logo": 'https://raw.githubusercontent.com/ptitchev/private_streamlit/main/source/logo.png', "link":'https://projet-chev.streamlit.app/TCP1'},
    {'name': "The Chev Party - volume 2", "date": "Juin 2024", "logo": 'https://raw.githubusercontent.com/ptitchev/private_streamlit/main/source/logo2.png', "link":'https://projet-chev.streamlit.app'}
]

def spawn_archive(archives=archives):
    st.divider()
    select_archive_menu = st.expander('Voir les archives')
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