"""
Models for Github.com's API
"""

from abc import ABC


# ABC = Abstract Base Class
class RepoStorable(ABC):
    pass


class User:
    def __init__(self, dictionary):
        if isinstance(dictionary, dict):
            self.id = dictionary.get('id', None)
            self.login = dictionary.get('login', None)
            self.avatar_url = dictionary.get('avatar_url', None)
        else:
            raise ValueError


class GithubRepository(RepoStorable):
    def __init__(self, dictionary):
        if isinstance(dictionary, dict):
            self.id = dictionary.get('id', None)
            self.name = dictionary.get('name', None)
            self.description = dictionary.get('description', None)
            self.api_url = dictionary.get('url', None)
            self.site_url = dictionary.get('html_url', None)
            self.created_date = dictionary.get('created_at', None)
            self.last_updated = dictionary.get('updated_at', None)
            try:
                self.owner = User(dictionary.get('owner', None))
            except ValueError:
                self.owner = None
        else:
            raise ValueError


# TODO: Fill out this class
class BitbucketRepository(RepoStorable):
    def __init__(self):
        pass
