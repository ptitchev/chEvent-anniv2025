from session_state.session_state_elements import SessionStateElement, session_user, user_event, user_event_status


class SessionStateManager:
    def __init__(self):
        self.session_user = session_user
        self.user_event = user_event
        self.user_event_status = user_event_status
        self.is_init = False

    def manage_session_state(self):
        if not self.is_init :
            self.session_user.reset_session_state()
            self.user_event.reset_session_state()
            self.user_event_status.reset_session_state()
            self.is_init = True