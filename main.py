from session_state import SessionStateManager
from router import RouterManager

import streamlit as st

session_state_manager = SessionStateManager()
router_manager = RouterManager()

if __name__ == "__main__":

    session_state_manager.manage_session_state()
    router_manager.get_content()

