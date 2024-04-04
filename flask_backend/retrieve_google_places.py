import googlemaps
import os
from dotenv import load_dotenv

load_dotenv()

places_api_key = os.getenv("PLACES_API_KEY")

def get_top_places(location, activity):
    gmaps = googlemaps.Client(key=places_api_key)
    query = f"{activity} in {location}"
    results = gmaps.places(query=query)
    list_of_places = []

    for place in results['results']:
        name = place['name']
        place_id = place['place_id']
        rating = place.get('rating', 0)
        user_ratings_total = place.get('user_ratings_total', 0)
        maps_link = f"https://www.google.com/maps/search/?api=1&query=Google%20Maps&query_place_id={place_id}"
        list_of_places.append([name, place_id, rating, user_ratings_total, maps_link])

    # Sort the places based on user_ratings_total and rating
    sorted_places = sorted(list_of_places, key=lambda x: (-x[3], -x[2]))

    return sorted_places[:3]

# def get_top_places(location, activity):
#     gmaps = googlemaps.Client(key=places_api_key)
#     query = f"{activity} in {location}"
#     results = gmaps.places(query=query)
#     list_of_places = []

#     for place in results['results']:
#         name = place['name']
#         place_id = place['place_id']
#         rating = place.get('rating', 0)
#         user_ratings_total = place.get('user_ratings_total', 0)
#         list_of_places.append([name, place_id, rating, user_ratings_total])

#     # Sort the places based on user_ratings_total and rating
#     sorted_places = sorted(list_of_places, key=lambda x: (-x[3], -x[2]))

#     return sorted_places[:3]