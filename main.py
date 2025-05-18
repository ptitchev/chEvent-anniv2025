from database.create import create_tables
from database.init import init_db
from topics.runner import init_state, run_page, add_common_style, st_db_health

reset = False
update = False

if reset:
    init_db()
elif update:
    create_tables()

if st_db_health():
    init_state()
    run_page()
    add_common_style()