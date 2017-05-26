import requests


class User:
    def __init__(self, dictionary):
        if isinstance(dictionary, dict):
            self.id = dictionary.get('id', None)
            self.login = dictionary.get('login', None)
        else:
            raise ValueError


class CodeRepository:
    def __init__(self, dictionary):
        if isinstance(dictionary, dict):
            self.id = dictionary.get('id', None)
            self.name = dictionary.get('name', None)
            self.description = dictionary.get('description', None)
            self.url = dictionary.get('url', None)
            self.created_date = dictionary.get('created_at', None)
            self.last_updated = dictionary.get('updated_at', None)
            self.owner = User(dictionary.get('owner', None))
        else:
            raise ValueError


r = requests.get('https://api.github.com/users/mnorth719/repos')
repos = []
for item in r.json():
    try:
        repos.append(CodeRepository(item))
    except ValueError:
        print("Error parsing repository")

for repo in repos:
    print(repo.name or "None")