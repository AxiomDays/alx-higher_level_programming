#!/usr/bin/python3
"""puts email using request"""
if __name__ == "__main__":
    import requests
    import sys

    param = {'q': sys.argv[1]}
    if (len(sys.argv) == 0):
        param = {'q': ""}
    r = requests.post('http://0.0.0.0:5000/search_user', data=param)
    try:
        resp = r.json()
        if (resp == {}):
            print("No result")
        else:
            print("[{}] {}".format(resp.get('id'), resp.get('name')))
    except ValueError:
        print("Not a valid JSON")
