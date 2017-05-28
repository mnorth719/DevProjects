"""
SQL Alchemy Table Definitions / Schema
"""

from database.manager import base_model
from sqlalchemy import Column, Integer, String, DateTime, Boolean



# ORM Class for Repositories
class Repository(base_model()):
    __tablename__ = 'repositories'
    GITHUB_TYPE = 0
    BITBUCKET_TYPE = 1

    # API VALUES
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String)
    api_url = Column(String)    # Api URL to access the repo api detail page
    site_url = Column(String)   # Browser Url
    created_date = Column(DateTime)
    last_updated = Column(DateTime)


    # CUSTOM VALUES
    repo_type = Column(Integer)
    nickname = Column(String(255))      # Allow for a custom nickname to be set on the repo.
    should_display = Column(Boolean)    # Allow the repo to be hidden on the site
    is_private = Column(Boolean)    # Flag for whether or not the repo is private