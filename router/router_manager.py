from session_state import SessionStateManager
import streamlit as st
from content import connect_page, user_home_page, event_printer


class RouterManager:

    def __init__(self):
        self.session_state_manager = SessionStateManager()
        self.connect_page = connect_page
        self.user_home_page = user_home_page
        self.event_printer = event_printer

    def get_content(self):


        if st.session_state[self.session_state_manager.session_user.name] is None:
            self.connect_page.show()
        if st.session_state[self.session_state_manager.session_user.name] is not None:
            if st.session_state[self.session_state_manager.user_event.name] is None:
                self.user_home_page.show()
            else:
                self.event_printer.show()

        

    #if st.session_state["user"]:
        #if "selected_event" in st.session_state:
            #event_page()
        #else:
            #home_page()
    #else:
        #login_page()