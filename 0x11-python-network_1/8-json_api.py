#!/usr/bin/python3
"""
Sends a POST request to URL with a letter
as a parameter and processes the response
"""

import requests
import sys


def search_user(letter):
    """
    Sends a POST request to search_user endpoint
    and processes the response
    """
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': letter}
    response = requests.post(url, data=data)

    try:
        json_response = response.json()

        if json_response:
            print(f"[{json_response['id']}] {json_response['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    search_user(letter)
