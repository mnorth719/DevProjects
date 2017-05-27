import requests
from models.repos import CodeRepository
import datetime

def acquire_github_repositories(username):
    r = requests.get('https://api.github.com/users/{}/repos'.format(username))
    repos = []
    for item in r.json():
        try:
            repos.append(CodeRepository(item))
        except ValueError:
            print("Error parsing repository")

    return repos

# This means only execute this code if someone is running this file directly.
# The difference being - if someone is simply importing this module to use its functionality
# It won't run what's below.
if __name__ == "__main__":
    # Test purposes
    repositories = acquire_github_repositories("thingdeux")
    for repository in repositories:
        print(repository.owner.login)