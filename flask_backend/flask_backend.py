from flask import Flask, request, jsonify
from flask_cors import CORS
from spacy.matcher import Matcher
from activity_category_identifier import classify_activity_preference
from keywords_extractor import extract_keywords
from activity_label_mapper import extract_top_activities
from get_infectious_disease_data import get_year_graph_for_district
from city_to_district_mapper import get_district
from retrieve_google_places import get_top_places
from score_based_on_district import add_location_scores

app = Flask(__name__)
CORS(app)

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    user_prompt = data['term']

    location = None
    friend_count = None
    date = None
    activity_preference = None
    prioritized_activities = None
    district = None
    district_filtered_recommendation = None
    places_recommendation = []

    location,date,activity_preference = extract_keywords(user_prompt)
    # activity_preference = "gaming activities"

    if (location and activity_preference):
        prioritized_activities = classify_activity_preference(location,activity_preference)
        print(prioritized_activities)
        district = get_district(location)
        print("District is : " + str(district))
        if (district):
            district_filtered_recommendation = add_location_scores(prioritized_activities, district)
            print(district_filtered_recommendation)
            if (district_filtered_recommendation):
                for label,score in district_filtered_recommendation:
                    places_recommendation.append(get_top_places(location,str(label)))
                    print(places_recommendation)
        


    if district:
        plot_data = get_year_graph_for_district(district)
        return jsonify({
            'location': location,
            'activity_preference': activity_preference,
            'district': district,
            'top_activity_types': district_filtered_recommendation,
            'top_activities': places_recommendation,
            'plot_data': plot_data
        }), 200
    return jsonify({
        'location': location,
        'activity_preference': activity_preference,
        'top_activity_types': district_filtered_recommendation,
        'top_activities': places_recommendation
    }), 200

if __name__ == '__main__':
    app.run(debug=True)