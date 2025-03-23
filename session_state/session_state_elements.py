import streamlit as st

class SessionStateElement:
    def __init__(self, name, default, values=None):
        self.name = name
        self.default = default
        self.values = values
        self.reset_session_state()

    def reset_session_state(self):
        if self.name not in st.session_state:
            st.session_state[self.name] = self.default

    def update_session_state(self, value):
        if self.values is None or (value in self.values):
            st.session_state[self.name] = value

    def get_session_state(self):
        return st.session_state[self.name]

session_user = SessionStateElement("user", default=None)
user_event = SessionStateElement("user_event", default=None)
user_event_status = SessionStateElement("user_event_status", default=None)