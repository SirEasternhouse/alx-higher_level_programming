#!/usr/bin/python3
"""Uses Basic Authentication with GitHub API to display the user's id"""

import requests
import sys


def get_github_user_id(username, password):
    """Fetches the GitHub user ID using Basic Authentication"""
    url = 'https://api.github.com/user'
    auth = (username, password)
    response = requests.get(url, auth=auth)

    if response.status_code == 200:
        user_id = response.json()['id']
        print(f"GitHub User ID: {user_id}")
    else:
        print(f"GitHub User ID. Status code: {response.status_code}")


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    get_github_user_id(username, password)
