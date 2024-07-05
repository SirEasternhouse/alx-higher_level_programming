#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL,
and displays the value of the X-Request-Id variable in the response header
"""


import urllib.request
import sys


def fetch_x_request_id(url):
    """Fetches the X-Request-Id from the response header of the URL """
    with urllib.request.urlopen(url) as response:
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_x_request_id(url)
