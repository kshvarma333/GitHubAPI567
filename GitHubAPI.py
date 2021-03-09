import requests
import json

def git_hub_api(name_of_repo:str) -> list:
    answer:list = []
    url:str = f"https://api.github.com/users/{name_of_repo}/repos"
    list_of_repos: list = requests.get(url).json()
    for item in list_of_repos:
        repo_name = item['name']
        url2:str = f"https://api.github.com/repos/{name_of_repo}/{item['name']}/commits"
        list_of_commits:list = requests.get(url2).json()
        count = len(list_of_commits)
        temp:str = f'Repo: {repo_name} Number of commits: {count}'
        answer.append(temp)
    return answer

