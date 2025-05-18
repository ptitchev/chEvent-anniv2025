import streamlit as st

from topics.constants import INVITATION_STATUS

COLOR_FOR_STATUS = {
    INVITATION_STATUS.ACCEPT.value: '#4CAF50',
    INVITATION_STATUS.WAITING.value: '#FF9800',
    INVITATION_STATUS.REFUSED.value: '#F44336',
}

def spawn_status_displayer(user_status):
    color = COLOR_FOR_STATUS.get(user_status, '#000000')
    return  st.markdown(
        f"""<strong style="color:{color}">
                {user_status}
            </strong>
        """,
        unsafe_allow_html=True
    )

def spawn_status_changer(user_status):
    possible_status = list(COLOR_FOR_STATUS.keys())
    user_status_index = possible_status.index(user_status)
    return st.radio(
        label="Ton choix",
        options=possible_status,
        index=user_status_index,
        horizontal=True
    )

def spawn_guests_status_filter(guests):
    order_status = list(COLOR_FOR_STATUS.keys())
    status_filter = st.segmented_control(
        "Filtre",
        order_status,
        selection_mode='multi',
        key="filtre"
    )
    if len(status_filter) > 0:
        filtered_users = [
            user
            for user in guests
            if user.user_status in status_filter
        ]
    else:
        filtered_users = guests

    filtered_users.sort(
        key=lambda user: order_status.index(user.user_status)
    )

    for user in filtered_users:
        color = COLOR_FOR_STATUS.get(user.user_status, '#000000')
        st.markdown(
            f"""
                <div style="border: 1px solid #ddd; padding: 10px; border-radius: 10px; margin-bottom: 10px; background-color: #f9f9f9;">
                    <strong>👤 {user.username}</strong>  
                    <span style="color: {color}">
                        - {user.user_status}
                    </span>  
                </div>
            """,
            unsafe_allow_html=True,
        )
