import googlemaps
import pprint
import time
import os
from operator import itemgetter
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access API key
places_api_key = os.getenv("PLACES_API_KEY")

# define the Client
gmaps = googlemaps.Client(key = places_api_key)

# Example text search
query = 'park in colombo'
results = gmaps.places(query=query)

print(results)
location = []
list_of_locations = []
for place in results['results']:
    print(f"Name: {place['name']}, Place ID: {place['place_id']}, Rating: {place['rating']}, Total user ratings : {place['user_ratings_total']}")
    location = [place['name'],place['place_id'],place['rating'],place['user_ratings_total']]
    list_of_locations.append(location)
sorted_places = sorted(list_of_locations, key=itemgetter(3), reverse=True)
print(sorted_places[:3])