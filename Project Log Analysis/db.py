# Import Required Library
from contextlib import contextmanager
import psycopg2


@contextmanager
def db_session_context(db_name):
    ''' Using context manager to ensure the database connection
    is fully closed when out of scope '''
    try:
        db = psycopg2.connect(database=db_name)
        yield db
    finally:
        db.close()