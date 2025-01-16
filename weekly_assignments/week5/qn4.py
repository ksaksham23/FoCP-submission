"""
Write a program that takes a URL as a command-line argument and reports
whether or not there is a working website at that address.
"""

import sys
import requests

user_url = sys.argv[1]

response = requests.get(user_url)

if response.status_code == 200:
    print(f"{user_url} is a working website. Status code ={response.status_code}")
else:
    print(f"{user_url} not a functioning websit. Status Code ={response.status_code}")
