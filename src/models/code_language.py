"""
Model for coding language
"""

from abc import ABC


# ABC = Abstract Base Class
class LanguageStorable(ABC):
    pass


class CodeLanguage(LanguageStorable):
    def __init__(self, dictionary: dict):
        self.id = dictionary.get('id', None)
        self.name = dictionary.get('name', None)
        self.textColor = dictionary.get('textColor', None)
