#!/usr/bin/python3
"""
Takes in a URL and an email address,
sends a POST request to the URL with the email as a parameter,
and displays the body of the response
"""

import requests
import sys


def send_post_request(url, email):
    """
    Sends a POST request to the URL with the email
    as a parameter and prints the response body
    """
    data = {'email': email}
    response = requests.post(url, data=data)
    print(response.text)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)
