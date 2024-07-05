#!/usr/bin/python3
"""Fetches URL the requests package and displays the response"""

import requests


def fetch_status():
    """Fetches the status from the URL and prints the response details"""
    url = 'https://alx-intranet.hbtn.io/status'

    response = requests.get(url)

    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)


if __name__ == "__main__":
    fetch_status()
