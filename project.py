'''
Copyrights 2020, 15/06/2020

[Authors]
Chethan Jagannatha Kulkarni - 1BY17EC037 - Director,CTO at Mazon Technologies
Hussain S. G - 1BY17EC062
'''
from urllib import request
import json

'''
All the data is requested from GitHub API v3
'''

class Github:
    '''
    Initialize the class with a GitHub username
    '''
    def __init__(self, username=None, *args, **kwargs):
        self._public_repos = []
        self.username = username
        if not username:
            raise ValueError("GitHub username is required")
        repos = request.urlopen("https://api.github.com/users/{}".format(username))
        for f in repos:
            parsed_data = json.loads(f)
        print("Name: {}".format(parsed_data["name"]))
        print("Twitter Username: {}".format(parsed_data["twitter_username"]))
        print("Total public repos: {}".format(parsed_data["public_repos"]))
        print("Repositories URL: {}".format(parsed_data["repos_url"]))

    
    @property
    def public_repos(self):
        '''
        Gets the repository urls of the given username
        '''
        public_repos_object = request.urlopen("https://api.github.com/users/{}/repos".format(self.username))
        for data in public_repos_object:
            repos = json.loads(data)
        for repo in repos:
            self._public_repos.append(repo["html_url"])
        return self._public_repos


if __name__ == "__main__":
    g = Github(username=input("Enter GitHub username: "))
    print(g.public_repos)