all_tables = ["user_event", "events", "users"]


def drop_table(cursor, table):
    cursor.execute(
        f"""
        DROP TABLE IF EXISTS {table};
        """
    )

def drop_all_tables(cursor, all_tables=all_tables):
    for table in all_tables:
        drop_table(cursor, table)

def create_users(cursor):
    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        email VARCHAR(100),
        username VARCHAR(50) UNIQUE NOT NULL,
        password_hash VARCHAR(255) NOT NULL
    );"""
    )
                   

def create_events_table(cursor):
    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS events (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        date DATE,
        location VARCHAR(100),
        create_user_id INT REFERENCES users(id)
    );
    """)

def create_user_event_table(cursor):
    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS user_event (
        id SERIAL PRIMARY KEY,
        user_id INT REFERENCES users(id),
        event_id INT REFERENCES events(id),
        status VARCHAR(100) NOT NULL,
        message VARCHAR(255),
        UNIQUE(user_id, event_id)
    );
    """
    )

def create_all_tables(cursor):
    create_users(cursor)
    create_events_table(cursor)
    create_user_event_table(cursor)