import requests

keyword = input("Enter keyword: ")

request = "https://api.tvmaze.com/search/shows?q=" + keyword
try:
    response = requests.get(request)
    print(response)

    if response.ok:
        tv_shows = response.json()
        #print(json.dumps(tv_shows, indent=2))   #to test
        #json - javascript............notation

        for tv_shows in tv_shows:
            name = tv_shows['show']['name']
            print(f"Name: {name}")

    else:
        print("Error occurred")

except requests.exceptions.ConnectionError as error:
    print(error)