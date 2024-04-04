import nltk
import spacy
from spacy.matcher import Matcher

def extract_keywords(user_prompt):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(user_prompt)
    token_dep = ''
    token_labels = ''

    location = None
    friend_count = None
    date = None
    activity_preference = None

    matcher = Matcher(nlp.vocab)

    # Defined patterns for the specified locations
    location_patterns = [
        [{"LOWER": "colombo"}],
        [{"LOWER": "sri"}, {"LOWER": "jayewardenepura"}, {"LOWER": "kotte"}],
        [{"LOWER": "mount"}, {"LOWER": "lavinia"}],
        [{"LOWER": "kesbewa"}],
        [{"LOWER": "moratuwa"}],
        [{"LOWER": "maharagama"}],
        [{"LOWER": "ratnapura"}],
        [{"LOWER": "kandy"}],
        [{"LOWER": "negombo"}],
        [{"LOWER": "batticaloa"}],
        [{"LOWER": "mawanella"}],
        [{"LOWER": "trincomalee"}],
        [{"LOWER": "kalmunai"}],
        [{"LOWER": "kotmale"}],
        [{"LOWER": "kilinochchi"}],
        [{"LOWER": "hikkaduwa"}],
        [{"LOWER": "galle"}],
        [{"LOWER": "jaffna"}],
        [{"LOWER": "athurugiriya"}],
        [{"LOWER": "weligama"}],
        [{"LOWER": "tangalla"}],
        [{"LOWER": "kolonnawa"}],
        [{"LOWER": "matara"}],
        [{"LOWER": "gampaha"}],
        [{"LOWER": "akurana"}],
        [{"LOWER": "anuradhapura"}],
        [{"LOWER": "puttalam"}],
        [{"LOWER": "badulla"}],
        [{"LOWER": "matale"}],
        [{"LOWER": "kalutara"}],
        [{"LOWER": "bentota"}],
        [{"LOWER": "mannar"}],
        [{"LOWER": "mabole"}],
        [{"LOWER": "pothuhera"}],
        [{"LOWER": "kurunegala"}],
        [{"LOWER": "nuwara"}, {"LOWER": "eliya"}],
        [{"LOWER": "hatton"}],
        [{"LOWER": "galhinna"}],
        [{"LOWER": "hambantota"}],
        [{"LOWER": "abasingammedda"}],
        [{"LOWER": "kalpitiya"}],
        [{"LOWER": "tissamaharama"}],
        [{"LOWER": "dambulla"}],
        [{"LOWER": "galgamuwa"}],
        [{"LOWER": "dikwella"}, {"LOWER": "south"}],
        [{"LOWER": "kalawana"}],
        [{"LOWER": "nikaweratiya"}],
        [{"LOWER": "bakamune"}],
        [{"LOWER": "sevanagala"}],
        [{"LOWER": "vavuniya"}],
        [{"LOWER": "gampola"}],
        [{"LOWER": "mullaittivu"}],
        [{"LOWER": "point"}, {"LOWER": "pedro"}],
        [{"LOWER": "hakmana"}],
        [{"LOWER": "kegalle"}],
        [{"LOWER": "gandara"}, {"LOWER": "west"}],
        [{"LOWER": "monaragala"}],
        [{"LOWER": "panadura"}],
        [{"LOWER": "rajagiriya"}],
        [{"LOWER": "kosgama"}],
        [{"LOWER": "keselwatta"}],
        [{"LOWER": "galkissa"}]
    ]

    # Defined patterns for the day
    date_patterns = [
        [{"LOWER": "tomorrow"}],
        [{"LOWER": "tmrw"}],
    ]

    matcher.add("GPE", location_patterns)
    matcher.add("DATE", date_patterns)


    for sentence in doc.sents:
        for token in sentence:
            token_dep += str(token.dep_) + " "
            if token.dep_ in ('cc','relcl'):
                conj_act_pref_index = token.i
                activity_preference = sentence[conj_act_pref_index:].text

    if activity_preference == None:
        activity_preference = input("Please enter what sort of activity you would like: ")
    print(token_dep)
    print("Activity preference phrase is : " + str(activity_preference))

    for ent in doc.ents:
        token_labels += str(ent.label_) + " "
        # Identify location and date based on named entity recognition (NER)
        if ent.label_ == "GPE" and location is None:
            location = ent.text
        elif ent.label_ == "DATE" and date is None:
            date = ent.text

    if location is None or date is None:
        matches = matcher(doc)
        for match_id, start, end in matches:
            string_id = nlp.vocab.strings[match_id]
            span = doc[start:end] 
            if doc.vocab.strings[match_id] == "GPE":
                location = span.text
            if doc.vocab.strings[match_id] == "DATE":
                date = span.text                
    print("Location is : " + str(location))
    print("Date is : " + str(date))
    return location,date,activity_preference


