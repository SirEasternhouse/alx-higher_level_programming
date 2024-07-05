#!/usr/bin/python3
"""
Handles HTTP status codes greater than or equal to
400 and prints an error message.
"""

import requests
import sys


def fetch_url_content(url):
    """Fetches the content of the URL and prints it, handling HTTP errors."""
    response = requests.get(url)

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_url_content(url)
