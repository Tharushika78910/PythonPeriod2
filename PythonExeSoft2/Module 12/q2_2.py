from datetime import datetime
import requests
from Ex12_APIkey import open_weather

def open_weather_map(city):
    server = "https://api.openweathermap.org"
    request = server + "/data/2.5/weather" + "?q=" + city + "&appid=" + open_weather()
    response = requests.get(request)
    return response.status_code, requests.get(request).json()

def temp_in_cel(kelvin):
    return kelvin - 273.15

city = input("In which city do you want to check weather : ")

try:
    (result, data) = open_weather_map(city)
    if result == 200:
        print(f"Current weather: {data['weather'][0]['description']}, "
              f"Temperature: {temp_in_cel(data['main']['temp']):.1f} ")
    elif result == 401:
        print("This is not a valid API key")
    elif result == 404:
        print("There is no weather info for "+city)
    else:
        print("Unknown response code "+ str(result))

except requests.exceptions.RequestException as e:
    print("Request cannot be completed")