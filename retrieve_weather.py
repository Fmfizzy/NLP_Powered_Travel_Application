import requests
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()
weather_api_key = os.getenv("WEATHER_API_KEY")

location = 'Colombo'
# Make a GET request to the API
if len(location) != 0:
    response_lat = requests.get('http://api.openweathermap.org/geo/1.0/direct?q='+ str(location) + '&limit=1&appid='+ str(weather_api_key))

    if (response_lat.status_code == 200):
        # Parse the JSON response
        data = response_lat.json()
        if data != []:
            print(data[0]['lat'])
            print(data[0]['lon'])
            response_weather = requests.get('http://api.openweathermap.org/data/2.5/forecast?lat='+ str(data[0]['lat']) +'&lon='+ str(data[0]['lon']) +'&appid='+ str(weather_api_key))
            print(response_weather)
        else:
            print("Sorry cannot retrieve latitude and longitude values for given city")

