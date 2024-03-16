#!/usr/bin/python3
"""puts email using request"""
if __name__ == "__main__":
    import requests
    import sys
    r = requests.put(sys.argv[1], data{'email': sys.argv[2]})
    print(r.text)
