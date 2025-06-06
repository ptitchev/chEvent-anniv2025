from enum import Enum

class PAGE_NAMES(Enum):
    CONNECT = "connect"
    HOME = "home"
    EVENT = "event"

class STATE_ELEMENTS(Enum):
    PAGE_NAME = "page_name"
    USERNAME = "user_name"
    EVENT_ID = "event_id"

class CONNECT_MESSAGES(Enum):
    SUCCESS = "success"
    UNKNOWN = "unknown"
    INVALID = "invalid"

class INVITATION_STATUS(Enum):
    ACCEPT = "Accepté"
    WAITING = "Attente de réponse"
    REFUSED = "Refusé"
    ORGANISATOR = "Organisateur"
