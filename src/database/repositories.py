"""
 Github.com DB CRUD.
"""

import database.manager as db_manager
from database.models.repository import Repository
from models.repos import GithubRepository, BitbucketRepository, RepoStorable
from dateutil.parser import parse as date_parser


class Actions:

    @staticmethod
    def insert_new_code_repo(code_repo: RepoStorable):
        if isinstance(code_repo, GithubRepository):
            try:
                github_db_object = Actions._map_github_repo_to_orm_object(code_repo)
                if github_db_object:
                    session = db_manager.get_session()
                    session.add(github_db_object)
                    session.commit()
            except AttributeError:
                print("Unable to save Github Repo Object - missing required attributes")
        elif isinstance(code_repo, BitbucketRepository):
            raise NotImplemented

    @staticmethod
    def update_code_repo(code_repo: RepoStorable):
        # Query repo (by Id) and update its value on the DB.
        if isinstance(code_repo, GithubRepository):
            try:
                session = db_manager.get_session()
                repo = session.query(Repository).filter(Repository.id == code_repo.id).one_or_none()
                if repo:
                    # If attributes are not filled out on the updating code repository, use the currently
                    # stored attribute as a fallback.
                    repo.name = code_repo.name or repo.name
                    repo.description = code_repo.description or repo.description
                    repo.api_url = code_repo.api_url or repo.url
                    repo.site_url = code_repo.site_url or repo.site_url

                    created_date = date_parser(code_repo.created_date)
                    last_updated = date_parser(code_repo.last_updated)
                    repo.created_date = created_date or repo.created_date
                    repo.last_updated = last_updated or repo.last_updated

                    session.commit()
                    print("Updated code repo {}".format(code_repo.id))
            except AttributeError as e:
                print("Unable to update repository - missing attribute: {}".format(e))

    @staticmethod
    def delete_code_repo(repo_id: int):
        # Delete repostiroy stored locally
        raise NotImplemented

    @staticmethod
    def get_code_repo(repo_id: int) -> Repository:
        # Query the DB for a given code repository
        session = db_manager.get_session()
        return session.filter(Repository.id == repo_id)

    # Private Methods
    @staticmethod
    def _map_github_repo_to_orm_object(repo: GithubRepository) -> Repository:
        """
        Take a API GithubRepository class object and convert it into a DB Repository object

        :param repo: GithubRepository (API Object)
        :return: Repository
        """
        if repo.id and repo.name and repo.site_url:
            repo_to_return = Repository(id=repo.id, name=repo.name, site_url=repo.site_url,
                                         api_url=repo.api_url, description=repo.description)

            repo_to_return.repo_type = Repository.GITHUB_TYPE
            if repo.created_date:
                parsed_created = date_parser(repo.created_date)
                repo_to_return.created_date = parsed_created
            if repo.last_updated:
                parsed_last_updated = date_parser(repo.last_updated)
                repo_to_return.last_updated = parsed_last_updated

            return repo_to_return
        else:
            raise AttributeError
