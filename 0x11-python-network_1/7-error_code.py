#!/usr/bin/python3
"""fetches"""

import requests
import sys

if __name__ == "__main__":
    try:
        r = requests.get(sys.argv[1])
        print(r.text)
    except requests.exceptions.RequestException as e:
        print("Error code: {}".format(r.status_code))
