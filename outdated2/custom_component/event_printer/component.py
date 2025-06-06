import streamlit as st
import streamlit.components.v1 as components

import locale
locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')

_component_func = components.declare_component(
        "print_event",
        path="custom_component/event_printer/build",
    )

def spawn_print_event(event,key = None):
    eventName = event.name
    eventLocation = event.location
    eventDate = event.date.strftime("%d %B %Y")
    eventCreator = event.creator_username
    eventUserStatus = event.user_status
    eventFirstImage = event.first_image_link

    component_value = _component_func(
        eventName=eventName, 
        eventLocation=eventLocation,
        eventDate=eventDate,
        eventCreator=eventCreator,
        eventUserStatus=eventUserStatus,
        eventFirstImage=eventFirstImage,
        key=key
        )
    
    return component_value