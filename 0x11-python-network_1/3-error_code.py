#!/usr/bin/python3
"""takes in a url and return header"""
if __name__ == "__main__":
    import urllib.request
    import sys

    r = urllib.request.Request(sys.argv[1])
    try: 
        with urllib.request.urlopen(r) as resp:
            html = resp.read()
        print(html.decode('utf-8'))
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
