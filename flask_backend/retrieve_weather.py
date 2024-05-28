import requests
from pprint import pprint
import os
from dotenv import load_dotenv
import json
from datetime import datetime

load_dotenv()
weather_api_key = os.getenv("WEATHER_API_KEY")

def get_weather_info(location, date_str):
    if location == "NuwaraEliya":
        location = 'Nuwara Eliya'

    # Convert the date string to a datetime object
    try:
        date = datetime.strptime(date_str, '%Y/%m/%d')
    except ValueError:
        print(f"Invalid date format: {date_str}. Please use the 'YYYY/MM/DD' format.")
        return None

    # Make a GET request to the API to get the latitude and longitude
    response_lat = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid={weather_api_key}')
    
    if response_lat.status_code == 200:
        data = response_lat.json()
        if data:
            latitude = data[0]['lat']
            longitude = data[0]['lon']

            # Make a GET request to the API to get the weather forecast
            response_weather = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={weather_api_key}')
            response_json = response_weather.json()

            # Find the weather information for the given date
            weather_info = []
            for entry in response_json['list']:
                entry_date = datetime.strptime(entry['dt_txt'], '%Y-%m-%d %H:%M:%S')
                if entry_date.date() == date.date():
                    hour = entry_date.hour
                    if hour in [9, 12, 18]:  # Morning, noon, and evening
                        temperature = round(entry['main']['temp'] - 273.15, 1)
                        weather_description = entry['weather'][0]['description']
                        weather_icon = entry['weather'][0]['icon']
                        time = entry_date.strftime('%H:%M')
                        weather_info.append({
                            'time': time,
                            'temperature': temperature,
                            'weather': weather_description,
                            'icon': weather_icon
                        })
            if weather_info:
                return weather_info
            else:
                print(f"Sorry, no weather information found for {location} on {date_str}.")
                return None
        else:
            print("Sorry, cannot retrieve latitude and longitude values for the given city.")
            return None
    else:
        print("Error retrieving weather information.")
        return None