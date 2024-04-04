import googlemaps
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

places_api_key = os.getenv("PLACES_API_KEY")

# Initialize the Google Maps client
gmaps = googlemaps.Client(key=places_api_key)

# Place ID for which you want to get the price level
place_id = "ChIJN1t_tDeuEmsRUsoyG83frY4"

# Make a request to the Place Details API
place_result = gmaps.place(place_id=place_id, fields=['price_level'])

# Check if the price_level field is available
if 'price_level' in place_result['result']:
    price_level = place_result['result']['price_level']
    print(f"The price level of this place is: {price_level}")
else:
    print("Price level information is not available for this place.")
