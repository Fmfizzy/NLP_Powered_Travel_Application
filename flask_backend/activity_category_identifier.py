from transformers import pipeline, AutoModel, AutoTokenizer, AutoModelForSequenceClassification
from activity_label_mapper import extract_top_activities


def classify_activity_preference(location,activity_preference):
    # Load locally saved model
    loaded_model = AutoModelForSequenceClassification.from_pretrained("J:/IIT Folder/Year_4/FYP/Code/my_model")
    tokenizer = AutoTokenizer.from_pretrained("J:\IIT Folder\Year_4\FYP\Code\my_model")
    new_classifier = pipeline("zero-shot-classification", model=loaded_model,tokenizer=tokenizer)

    # classifier = pipeline("zero-shot-classification", model="MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli")
    sequence_to_classify = activity_preference
    candidate_labels = ["indoor", "outdoor","physical","non_physical", "engaging", "water", "budget", "luxury", "nature", "relaxing"]
    hypothesis_template = "The activity mentioned is {}."
    output = new_classifier(sequence_to_classify, candidate_labels, multi_label=True, hypothesis_template=hypothesis_template)
    print(output)

    sentiment, percentage = classify_sentiment(activity_preference, new_classifier)
    print("The activity preference is :"+ str(activity_preference) +"The sentiment is: " + str(sentiment) + " with a percentage of :" + str(percentage))
    
    top_3_labels = get_top_3_activities(output)
    if sentiment == "negative" and percentage > 0.5:
        top_3_labels_with_negation = []
        for label, score in top_3_labels:
            opp_label = map_opposite_terms(label)
            top_3_labels_with_negation.append((opp_label, score))
        top_10_activities = extract_top_activities(top_3_labels_with_negation)
        print(top_10_activities)
    else:
        top_10_activities = extract_top_activities(top_3_labels)
        print(top_10_activities)
    prioritized_activities= prioritize_activities(top_10_activities, new_classifier, activity_preference)
    return prioritized_activities

def get_top_3_activities(activity_categories):
    activity_category_list = list(zip(activity_categories['labels'], activity_categories['scores']))
    top_3_labels = activity_category_list[:3]
    return top_3_labels

def classify_sentiment(activity_preference, classifier):
    sequence_to_classify = activity_preference
    candidate_labels = ["positive", "negative"]
    hypothesis_template = "The requirement of this category is {}."
    output = classifier(sequence_to_classify, candidate_labels, multi_label=True, hypothesis_template=hypothesis_template)
    sentiment = output['labels'][0]
    percentage = output['scores'][0]
    return sentiment, percentage

def map_opposite_terms(predicted_label):
    opposite_terms = {
        'physical': 'non_physical',
        'non_physical': 'physical',
        'indoor': 'outdoor',
        'outdoor': 'indoor',
        'engaging': 'relaxing',
        'water': None,  # would need to create a seperate non water category
        'budget': 'luxury',
        'luxury': 'budget',
        'nature': 'indoor', 
        'relaxing': 'engaging'
    }
    if predicted_label in opposite_terms:
        mapped_label = opposite_terms[predicted_label]
        if mapped_label:
            return mapped_label            
        else:        
            return predicted_label            
    else:        
        return predicted_label
        
from typing import List, Tuple, Dict

def normalize_scores(scores: List[Tuple[str, float]]) -> List[Tuple[str, float]]:
    """Normalize scores to a range of 0 to 1."""
    max_score = max(score for _, score in scores)
    return [(activity, score / max_score) for activity, score in scores]

def prioritize_activities(top_10_activities: List[Tuple[str, float]], classifier, activity_preference: str) -> List[Tuple[str, float]]:
    prioritized_activities = []
    top_activities = [item[0] for item in top_10_activities]
    candidate_labels = top_activities
    hypothesis_template = "The best activity for this statement is {}."

    model_suggested_activities = classifier(activity_preference, candidate_labels, multi_label=True, hypothesis_template=hypothesis_template)
    print(model_suggested_activities)

    # Normalize scores from the first model (top_10_activities)
    normalized_first_model_scores = normalize_scores(top_10_activities)

    # Normalize scores from the second model (model_suggested_activities)
    max_second_model_score = max(model_suggested_activities['scores'])
    normalized_second_model_scores = {label: score / max_second_model_score for label, score in zip(model_suggested_activities['labels'], model_suggested_activities['scores'])}

    for activity, first_model_score in normalized_first_model_scores:
        second_model_score = normalized_second_model_scores.get(activity, 0.0)
        combined_score = 0.5 * first_model_score + 0.5 * second_model_score
        prioritized_activities.append((activity, combined_score))

    prioritized_activities.sort(key=lambda x: x[1], reverse=True)
    return prioritized_activities
