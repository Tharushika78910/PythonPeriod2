import requests
import json

server = "https://api.chucknorris.io"
request = server + "/jokes/random"

try:
    response = requests.get(request).json()
    #print(json.dumps(response, indent=2))
    print(response["value"])
except requests.exceptions.ConnectionError as e:
    print("Request could not be completed", e)