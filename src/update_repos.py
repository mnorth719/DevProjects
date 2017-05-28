import requests
from models.repos import GithubRepository
from sqlalchemy.exc import IntegrityError as SQLIntegrityError


def acquire_github_repositories(username) -> [GithubRepository]:
    r = requests.get('https://api.github.com/users/{}/repos'.format(username))
    repos = []
    for item in r.json():
        try:
            repos.append(GithubRepository(item))
        except ValueError:
            print("Error parsing repository")

    return repos

# This means only execute this code if someone is running this file directly.
# The difference being - if someone is simply importing this module to use its functionality
# It won't run what's below.
if __name__ == "__main__":
    from database.repositories import Actions as db_actions
    from database.manager import check_db_exists

    # Test purposes
    check_db_exists()
    repositories: [GithubRepository] = acquire_github_repositories("thingdeux")

    for repository in repositories:
        try:
            db_actions.insert_new_code_repo(repository)
        except SQLIntegrityError as e:
            db_actions.update_code_repo(repository)