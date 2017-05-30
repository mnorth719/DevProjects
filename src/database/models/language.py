"""
SQL Alchemy Table Definitions / Schema
"""

from database.manager import base_model
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship


repo_language_table = Table('RepositoryLanguages', base_model().metadata,
    Column('repo_id', Integer, ForeignKey('repositories.id')),
    Column('language_id', Integer, ForeignKey('languages.id'))
)


# ORM Class for Repositories
class Language(base_model()):

    __tablename__ = 'languages'

    id = Column(Integer, primary_key=True)
    textColor = Column(String(255))
    name = Column(String(255))
    repositories = relationship("Repository", secondary=repo_language_table, back_populates="languages")
