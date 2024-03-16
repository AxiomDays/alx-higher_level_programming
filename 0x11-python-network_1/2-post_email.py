#!/usr/bin/python3
"""takes in a url and sends email"""
if __name__ == "__main__":
    import urllib.parse
    import urllib.request
    import sys

    
    values = {'email' : sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    r = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(r) as resp:
        page = resp.read()
    print(page.decode('utf-8'))
