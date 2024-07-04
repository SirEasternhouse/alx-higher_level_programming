#!/bin/bash
# This script takes a URL, sends a GET request, and displays the body of a 200 status code response
curl -sL -w "%{http_code}" "$1" -o /dev/null | grep -q "200" && curl -sL "$1"
