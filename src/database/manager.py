# Database management.
# Responsible for:
#   1. Making sure DB exists and is running
#   2. Safe wrapper around lower level DB calls.
#   3. Simple interactions


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError as SQLError
from sqlite3 import OperationalError as SQLiteError
import os

# Path to Root of Repository
DB_LOCATION = os.path.dirname(os.path.dirname(__file__))
_engine = create_engine('sqlite:////{db_location}/{db_name}'.format(db_location=DB_LOCATION, db_name='app.db'))
_Session = sessionmaker(bind=_engine)
_Base = declarative_base()


def base_model():
    return _Base

def get_session():
    return _Session()

def check_db_exists():
    # Inner import - prevent cyclic redundancy
    from database.models.repository import Repository
    from database.models.environment import ETagTracker, AppState

    try:
        repository_count = get_session().query(Repository).count()
        print("Found {} Stored Repositories".format(repository_count))
        tracker_count = get_session().query(ETagTracker).count()
        print("Found {} Trackers".format(tracker_count))
        get_session().query(AppState).count()
    # TODO: Fix this - don't catch everything
    except Exception:
        _Base.metadata.create_all(_engine)
        print("Creating Engine")
