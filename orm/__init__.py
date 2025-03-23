from orm.tables.users import Users
from orm.tables.events import Events
from orm.tables.user_event import UserEvent
from orm.config import DB_URL

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def connect_orm():
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    db_session = Session()
    return db_session