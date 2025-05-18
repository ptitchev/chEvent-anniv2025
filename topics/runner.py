from database.utils import dbUtils
from topics import PAGES
from topics.constants import PAGE_NAMES, STATE_ELEMENTS
import streamlit as st

def init_state():
    if STATE_ELEMENTS.PAGE_NAME.value not in st.session_state:
        st.session_state[STATE_ELEMENTS.PAGE_NAME.value] = PAGE_NAMES.CONNECT.value
    if STATE_ELEMENTS.USERNAME.value not in st.session_state:
        st.session_state[STATE_ELEMENTS.USERNAME.value] = None

def st_db_health():
    DB_URI = st.secrets["DB_URI"]
    if not dbUtils.health(DB_URI):
        st.error("Site non fonctionnel : Base de donnée indisponible.")
        return False
    else:
        return True

def run_page():
    page_name = st.session_state[STATE_ELEMENTS.PAGE_NAME.value]
    PageBuilder = PAGES[page_name]
    st.set_page_config(
        page_title=PageBuilder.page_title,
        page_icon=PageBuilder.page_icon,
        layout = "wide"
    )
    with st.container(key="int"):
        session = dbUtils.open_session()
        PageBuilder.build(session)

def add_common_style():
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

        .block-container {
            width: 100%;
            max-width: 660px;
            margin: auto;
            align-items: center;
            }

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

        div[data-testid="stTabs"] button {
            width: 100%;
            justify-content: center;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
        """,
        unsafe_allow_html=True
    )
