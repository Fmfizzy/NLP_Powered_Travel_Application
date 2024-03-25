import nltk
import spacy
from spacy.matcher import Matcher
from activity_category_identifier import classify_activity_preference
from keywords_extractor import extract_keywords
from activity_label_mapper import extract_top_activities

# user_prompt = input("Enter your prompt here : ")

location = None
friend_count = None
date = None
activity_preference = None

# location,date,activity_preference = extract_keywords(user_prompt)
activity_preference = "I would like some swimming activities for a day out"

labelled_activity_preference = classify_activity_preference(activity_preference)
print(labelled_activity_preference)

top_5_activities = extract_top_activities(labelled_activity_preference)
print(top_5_activities)



