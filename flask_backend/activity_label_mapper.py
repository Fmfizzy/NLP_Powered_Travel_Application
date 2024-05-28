weather_affected_activities = {"amusement_park","mountain_hiking","park","zoo","campground","swimming_pool","playground","beach","jogging_track","grounds","waterfall","Jetski","sports_complex"}

activity_category_dict = {
    "indoor": ["bowling_alley", "movie_theater", "bar", "cafe", "restaurant", "shopping_mall", "museum", "library","karaoke","futsal", "indoor_cricket","night_club","spa","gaming_cafe","badminton"],
    "outdoor": ["mountain_hiking", "park", "zoo","campground","swimming_pool","playground","beach","waterfall","water_sports","amusement_park","jogging_track"],
    "physical": ["bowling_alley","mountain_hiking","swimming_pool","futsal","indoor_cricket","grounds","sports_complex","playground","beach","jogging_track","badminton","park"],
    "non_physical": ["art_gallery","museum","library","movie_theater","aquarium","zoo","bar","cafe","restaurant","shopping_mall","karaoke","park","gaming_cafe","religous_sites"],
    "engaging": ["grounds","amusement_park","bowling_alley","badminton","gaming_cafe","karaoke","futsal","swimming_pool","beach","indoor_cricket","religous_sites","bar"],
    "water": ["aquarium","swimming_pool","beach", "fishing","waterfall","water_park","water_sports"],
    "budget":["library","park","restaurant","beach","grounds","cafe"],
    "luxury":["art_gallery","resteraunt","night_club","bar","spa","resort_hotel","water_sports", "casino"],
    "nature":["park","campground","mountain_hiking","waterfall","beach","safari"],
    "relaxing":["karaoke","park", "movie_theater", "cafe", "library","bowling", "museum", "art_gallery","religous_sites"]
}

indoor_priority_dict = {
    "bowling_alley": 2, 
    "movie_theater": 5, 
    "bar": 2,
    "cafe": 4, 
    "restaurant": 5, 
    "shopping_mall" : 2, 
    "museum": 1, 
    "library": 1,
    "karaoke": 5,
    "futsal": 2, 
    "indoor_cricket": 2,
    "night_club": 1,
    "spa": 1,
    "gaming_cafe": 4,
    "badminton": 2,
    "mountain_hiking": -5,
    "park": -5, 
    "zoo": -5,
    "campground": -5,
    "swimming_pool": -5,
    "playground": -5,
    "beach": -5,
    "waterfall": -5,
    "water_sports": -5,
    "amusement_park": -5,
    "jogging_track": -5
}

outdoor_priority_dict = {
    "mountain_hiking": 2,
    "park": 4, 
    "zoo": 3,
    "campground": 3,
    "swimming_pool": 4,
    "playground": 3,
    "beach": 5,
    "waterfall": 2,
    "water_sports": 2,
    "amusement_park": 3,
    "jogging_track": 3,
    "bowling_alley": -5, 
    "movie_theater": -5, 
    "bar": -5, 
    "cafe": -5, 
    "restaurant": -5, 
    "shopping_mall" : -5, 
    "museum": -5, 
    "library": -5,
    "karaoke": -5,
    "futsal": -5, 
    "indoor_cricket": -5,
    "night_club": -5,
    "spa": -5,
    "gaming_cafe": -5,
    "badminton": -5,
}

physical_priority_dict = {
    "bowling_alley": 3,
    "mountain_hiking": 3,
    "swimming_pool": 4,
    "futsal": 5,
    "indoor_cricket": 5,
    "grounds": 3,
    "sports_complex": 3,
    "playground": 3,
    "beach": 4,
    "jogging_track": 3,
    "badminton": 4,
    "park": 1,
    "art_gallery": -5,
    "museum": -5,
    "library": -5,
    "movie_theater": -5,
    "aquarium": -5,
    "zoo": -2,
    "bar": -5,
    "cafe": -5,
    "restaurant": -5,
    "shopping_mall": -4,
    "karaoke": -4,
    "gaming_cafe": -4
}

non_physical_priority_dict = {
    "art_gallery": 2,
    "museum": 1,
    "park": 4,
    "library": 1,
    "movie_theater": 5,
    "aquarium": 3,
    "zoo": 3,
    "bar": 2,
    "cafe": 4,
    "restaurant": 4,
    "shopping_mall": 3,
    "karaoke": 4,
    "gaming_cafe": 3,
    "religous_sites": 2,
    "bowling_alley": -4,
    "mountain_hiking": -5,
    "swimming_pool": -4,
    "futsal": -5,
    "indoor_cricket": -5,
    "grounds": -5,
    "sports_complex": -5,
    "playground": -5,
    "beach": -4,
    "jogging_track": -5,
    "badminton": -5,
}

engaging_priority_dict = {
    "grounds": 4,
    "amusement_park": 4,
    "bowling_alley": 5,
    "badminton": 3,
    "gaming_cafe": 3,
    "karaoke": 4,
    "futsal": 3,
    "swimming_pool": 2,
    "beach": 2,
    "indoor_cricket": 3,
    "religous_sites": 3,
    "bar": 3,
    "movie_theater": -5,
    "library": -4
}

water_priority_dict = {
    "aquarium": 3,
    "swimming_pool": 5,
    "beach": 3,
    "fishing": 2,
    "waterfall": 3,
    "water_park": 4,
    "water_sports": 4
}

budget_priority_dict = {
    "library": 3,
    "park": 4,
    "restaurant": 4,
    "beach": 4,
    "grounds": 3,
    "cafe": 3,
    "resort_hotel": -5,
    "casino": -5
}

luxury_priority_dict = {
    "art_gallery": 4,
    "restaurant": 4,
    "night_club": 5,
    "bar": 3,
    "spa": 3,
    "resort_hotel": 5,
    "water_sports": 3,
    "casino": 4,
    "beach": -5,
    "grounds": -5
}

nature_priority_dict = {
    "park": 4,
    "campground": 3,
    "mountain_hiking": 4,
    "waterfall": 3,
    "beach": 1,
    "safari": 3,
    "swimming_pool": -2,
    "movie_theater": -5,
    "amusement_park": -5,
    "bowling_alley": -5,
    "badminton": -5,
    "gaming_cafe": -5,
    "karaoke": -5,
    "futsal": -5,
}

relaxing_priority_dict = {
    "karaoke": 4,
    "park": 4,
    "movie_theater": 5,
    "cafe": 4,
    "library": 3,
    "bowling": 3,
    "museum": 2,
    "art_gallery": 2,
    "religous_sites": 3,
    "gaming_cafe": 3,
    "sports_complex": -5,
    "mountain_hiking": -5
}


def calculate_points(priority_dict, label_value, activity_points):
    for activity, score in priority_dict.items():
        points = label_value * score
        if activity_points != {} and activity in activity_points:
            activity_points[activity] += points
        else:
            activity_points[activity] = points
    return activity_points

def extract_top_activities(top_3_labels):
    # activity_category_list = list(zip(activity_categories['labels'], activity_categories['scores']))
    # top_3_labels = activity_category_list[:3]
    activity_points = {}

    activity_calculators = {
        'indoor': lambda value, points: calculate_points(indoor_priority_dict, value, points),
        'outdoor': lambda value, points: calculate_points(outdoor_priority_dict, value, points),
        'physical': lambda value, points: calculate_points(physical_priority_dict, value, points),
        'non_physical': lambda value, points: calculate_points(non_physical_priority_dict, value, points),
        'engaging': lambda value, points: calculate_points(engaging_priority_dict, value, points),
        'water': lambda value, points: calculate_points(water_priority_dict, value, points),
        'budget': lambda value, points: calculate_points(budget_priority_dict, value, points),
        'luxury': lambda value, points: calculate_points(luxury_priority_dict, value, points),
        'nature': lambda value, points: calculate_points(nature_priority_dict, value, points),
        'relaxing': lambda value, points: calculate_points(relaxing_priority_dict, value, points)
    }

    activity_points = {}
    for key, value in top_3_labels:
        activity_points = activity_calculators[key](value, activity_points)

    # sorted_activity_points_dict = dict(sorted(activity_points.items(), key=lambda item: item[1], reverse=True))

    top_10_activities = sorted(activity_points.items(), key=lambda item: item[1], reverse=True)[:10]
    return top_10_activities