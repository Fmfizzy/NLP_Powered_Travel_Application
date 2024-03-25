from transformers import pipeline, AutoModel, AutoTokenizer, AutoModelForSequenceClassification


def classify_activity_preference(activity_preference):
    # Load locally saved model
    loaded_model = AutoModelForSequenceClassification.from_pretrained("my_model")
    tokenizer = AutoTokenizer.from_pretrained("my_model")
    new_classifier = pipeline("zero-shot-classification", model=loaded_model,tokenizer=tokenizer)

    # classifier = pipeline("zero-shot-classification", model="MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli")
    sequence_to_classify = activity_preference
    candidate_labels = ["indoor", "outdoor","physical","non_physical", "engaging", "water", "budget", "luxury", "nature", "relaxing"]
    hypothesis_template = "The activity mentioned is {}."
    output = new_classifier(sequence_to_classify, candidate_labels, multi_label=True, hypothesis_template=hypothesis_template)
    sentiment, percentage = classify_sentiment(activity_preference, new_classifier)
    print("The sentiment is: " + str(sentiment) + " with a percentage of :" + str(percentage))
    return (output)

def classify_sentiment(activity_preference, classifier):
    sequence_to_classify = activity_preference
    candidate_labels = ["positive", "negative"]
    hypothesis_template = "The sentiment of this statement is {}."
    output = classifier(sequence_to_classify, candidate_labels, multi_label=True, hypothesis_template=hypothesis_template)
    sentiment = output['labels'][0]
    percentage = output['scores'][0]
    return sentiment, percentage