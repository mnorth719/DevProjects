"""
SQL Alchemy Table Definitions / Schema for App State Tracking
"""

from database.manager import base_model
from sqlalchemy import Column, Integer, String, DateTime, Boolean


# ORM Class for Repositories
class AppState(base_model()):
    __tablename__ = 'state'

    id = Column(Integer, primary_key=True, autoincrement=True)
    homepage_cache_last_refreshed = Column(DateTime)
    is_in_maintenance_mode = Column(Boolean)


class ETagTracker(base_model()):
    __tablename__ = 'etag_trackers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String, index=True) # ex: https://api.github.com/users/thingdeux/repos
    etag = Column(String(255))  # ex: d5d20d65e73e060c51275d8b0e3a480b