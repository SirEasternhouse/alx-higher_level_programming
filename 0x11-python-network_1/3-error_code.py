#!/usr/bin/python3
"""
Handles urllib.error.HTTPError exceptions
and prints the HTTP status code if an error occurs.
"""

import urllib.request
import urllib.error
import sys


def fetch_url_content(url):
    """Fetches the content of the URL and prints it, handling HTTP errors."""
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_url_content(url)
