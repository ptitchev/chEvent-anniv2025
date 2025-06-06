import time
import streamlit as st
import datetime

event_paris = {
    "name": "Soirée Parisienne",
    "date": datetime.date(2025, 6, 6),
    "location": "Paris - Apérock/Supersonic",
    'creator_username': "ptitchev",
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

st.set_page_config(
    page_title="chEvent : Soirée Parisienne",
    page_icon="🎉",
    layout = "wide"
)

with st.container(key="int"):
    st.markdown("<h1 style='text-align: center;'>🎉 chEvent : Soirée Parisienne</h1>", unsafe_allow_html=True)
    st.divider()
    st.write("A l'occasion de son 26ème anniversaire, le génial **Jules Chevenet** t'invites à faire la fête ce soir :")
    st.write("")
    gap1, col1, col2, col3, gap2 = st.columns([1, 2, 2, 2, 1])
    with col1:
        st.markdown(f"<div style='text-align: center;'>📍 {event_paris['location']}</div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div style='text-align: center;'>📅 19:00 - {event_paris["date"].strftime("%d %B %Y")}</div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div style='text-align: center;'>👤 {event_paris["creator_username"]}</div>", unsafe_allow_html=True)
    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        st.write(event_paris["description"])
        st.write("")
        st.write("⏳ **Compte à rebours**")
        event_date = datetime.datetime(2025, 6, 6, 19, 0)
        now = datetime.datetime.now()
        countdown = event_date - now
        days = countdown.days
        hours, remainder = divmod(countdown.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        placeholder = st.empty()
        st.write('')
        st.write("**Adresses**")
        st.markdown("[📍 Apérock - Google Maps](https://maps.app.goo.gl/pTrDEx3vq1DEqJUZ8)")
        st.markdown("[📍 Supersonic - Google Maps](https://maps.app.goo.gl/ChUsfbMTDw3wF6Cm9)")
        st.write("")
        st.write("**Motivé(e) ?**")
        feedback = st.feedback("thumbs")
        if feedback is not None:
            if feedback > 0:
                st.balloons()
    with col2:
        st.image(event_paris["first_image_link"], use_container_width =True, caption="L’ambiance de la soirée 🔥")

st.markdown("---")
st.markdown("💡 *Un pépin ? Contacte ptitchev !*")
st.markdown(
    """
        <style>
        .stApp {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f5;
        }

        .stApp > header {
            background-color: transparent;
        }

        .st-key-int {
            background-color:white;
            border-radius:1rem;
            padding:1rem;
            width: 100%;
            margin: 0 auto;
            box-sizing: border-box;
            overflow: hidden;
        }

        .st-key-int * {
            max-width: 100%;
            white-space: normal;
            word-wrap: break-word;
        }
    """,
    unsafe_allow_html=True
)


if countdown.total_seconds() <= 0:
    placeholder.success("🎉 C’est parti, la soirée commence !")
else:
    placeholder.markdown(f"""
        <h2 style='text-align: center; color: #8e44ad;'>
            {hours:02d}h :{minutes:02d}m :{seconds:02d}s
        </h2>
    """, 
    unsafe_allow_html=True)
time.sleep(1.5)
st.rerun()