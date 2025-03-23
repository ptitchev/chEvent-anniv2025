import streamlit as st

def global_show(show_int):
    st.session_state
    with st.container(key='int'):
        show_int()
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
            max-width: 510px;
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
                max-width: 510px;
                margin: auto;
                align-items: center;
            }
        """,
        unsafe_allow_html=True,
    )
    st.markdown("""
    <style>
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)
    st.markdown("""
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """, unsafe_allow_html=True)
