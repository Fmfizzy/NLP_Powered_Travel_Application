import nltk
import spacy
from spacy.matcher import Matcher
from activity_category_identifier import classify_activity_preference
from keywords_extractor import extract_keywords
from activity_label_mapper import extract_top_activities

# user_prompt = input("Enter your prompt here : ")

location = 'colombo'
friend_count = None
date = None
activity_preference = None

# location,date,activity_preference = extract_keywords(user_prompt)
activity_preference = "gaming activities"

prioritized_activities = classify_activity_preference(location, activity_preference)
print(prioritized_activities)

