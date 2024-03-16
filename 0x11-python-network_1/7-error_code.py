#!/usr/bin/python3
"""fetches"""

import requests
import sys

if __name__ == "__main__":
    try:
        r = requests.get(sys.argv[1])
        print(r.text)
    except r.raise_for_status() as e:
        print(e)
