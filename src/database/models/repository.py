"""
SQL Alchemy Table Definitions / Schema
"""

from database.manager import base_model
from sqlalchemy import Column, Integer, String, DateTime, Boolean

# ORM Class for Repositories
class Repository(base_model()):
    __tablename__ = 'repositories'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    nickname = Column(String(255))
    description = Column(String)
    url = Column(String)
    created_date = Column(DateTime)
    last_updated = Column(DateTime)
    should_display = Column(Boolean)
    is_private = Column(Boolean)