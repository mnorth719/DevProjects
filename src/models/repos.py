"""
Models for Github.com's API
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    def __init__(self, dictionary):
        if isinstance(dictionary, dict):
            self.id = dictionary.get('id', None)
            self.login = dictionary.get('login', None)
            self.avatar_url = dictionary.get('avatar_url', None)
        else:
            raise ValueError


class CodeRepository(Base):
    def __init__(self, dictionary):
        if isinstance(dictionary, dict):
            self.id = dictionary.get('id', None)
            self.name = dictionary.get('name', None)
            self.description = dictionary.get('description', None)
            self.url = dictionary.get('url', None)
            self.created_date = dictionary.get('created_at', None)
            self.last_updated = dictionary.get('updated_at', None)
            try:
                self.owner = User(dictionary.get('owner', None))
            except ValueError:
                self.owner = None
        else:
            raise ValueError