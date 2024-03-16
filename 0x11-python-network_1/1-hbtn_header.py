#!/usr/bin/python3
"""takes in a url and return header"""
if __name__ == "__main__":
    import urllib.request
    import sys

    r = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(r) as resp:
        page = resp.headers
    print(dict(page).get('X-Request-Id'))
