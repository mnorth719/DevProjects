#!/usr/bin/env python3.6

import requests
from models.repos import GithubRepository
from sqlalchemy.exc import IntegrityError as SQLIntegrityError


def acquire_github_repositories(username) -> [GithubRepository]:
    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'User-Agent': 'DevProjectBuilder-Python'
    }
    response = requests.get(url='https://api.github.com/users/{}/repos'.format(username), headers=headers)
    repos = []
    for item in response.json():
        try:
            repos.append(GithubRepository(item))
        except ValueError:
            print("Error parsing repository")

    return repos


def acquire_bitbucket_repositories(username):
    pass


# This means only execute this code if someone is running this file directly.
# The difference being - if someone is simply importing this module to use its functionality
# It won't run what's below.
if __name__ == "__main__":
    from database.repo_service import Actions as db_actions
    from database.manager import check_db_exists

    # Test purposes
    check_db_exists()
    repositories: [GithubRepository] = acquire_github_repositories("mnorth719")

    for repository in repositories:
        try:
            db_actions.insert_new_code_repo(repository)
        except SQLIntegrityError as e:
            db_actions.update_code_repo(repository)
