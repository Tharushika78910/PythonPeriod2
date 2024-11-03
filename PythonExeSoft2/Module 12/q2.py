import requests

lat=60
lon = 21
APIkey = "341123bcc1d83175fd559e2f091714a4"
request = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APIkey}&units=metric"
try:
    response = requests.get(request)

    if not response.ok:
        raise Exception('Resource Not found')

    weather = response.json()

    name = weather['name']
    temp = weather['main']['temp']
    print(f"Name: {name}")
    print(f"Temperature: {temp} Celsius")

except requests.exceptions.RequestException as error:
    print('Server not found')
except Exception as error:
    print(error)