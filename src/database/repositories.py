"""
 Github.com DB CRUD.
"""

import database.manager as db_manager
from database.models.repository import Repository
from models.repos import GithubRepository, BitbucketRepository, RepoStorable
from abc import ABC

class Actions:

    @staticmethod
    def insert_new_code_repo(code_repo: RepoStorable):
        if isinstance(code_repo, GithubRepository):
            github_db_object = Actions._map_github_repo_to_orm_object(code_repo)
            if github_db_object:
                session = db_manager.get_session()
                session.add(github_db_object)
                session.commit()
        elif isinstance(code_repo, BitbucketRepository):
            raise NotImplemented

    @staticmethod
    def update_code_repo(repo_id: int, code_repo: RepoStorable):
        # Query repo (by Id) and update its value on the DB.
        raise NotImplemented

    @staticmethod
    def delete_code_repo(repo_id: int):
        # Delete repostiroy stored locally
        raise NotImplemented

    @staticmethod
    def get_code_repo(repo_id: int):
        # Query the DB for
        raise NotImplemented


    # Private Methods
    @staticmethod
    def _map_github_repo_to_orm_object(repo: GithubRepository) -> Repository:
        if repo.id and repo.name and repo.url:
            return Repository(id=repo.id, name=repo.name, url=repo.url)
        else:
            return None