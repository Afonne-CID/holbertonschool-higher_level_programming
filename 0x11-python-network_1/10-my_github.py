#!/usr/bin/python3
"""Takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    value = requests.get("https://api.github.com/user", auth=auth)
    print(value.json().get("id"))
