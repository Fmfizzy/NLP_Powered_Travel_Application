import nltk
import spacy
import re
from datetime import datetime, timedelta
import parsedatetime as pdt
from spacy.matcher import Matcher

def extract_keywords(user_prompt):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(user_prompt)
    token_dep = ''
    token_labels = ''
    date_set = False

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
        [{"LOWER": "dikwella"}],
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
        [{"LOWER": "gandara"}],
        [{"LOWER": "monaragala"}],
        [{"LOWER": "panadura"}],
        [{"LOWER": "rajagiriya"}],
        [{"LOWER": "kosgama"}],
        [{"LOWER": "keselwatta"}],
        [{"LOWER": "galkissa"}],
        [{"LOWER": "polonnaruwa"}],
        [{"LOWER": "medirigiriya"}],
        [{"LOWER": "kilinochchi"}],
        [{"LOWER": "mannar"}],
        [{"LOWER": "dehiwala"}]
    ]

    # Defined patterns for the day
    date_patterns = [
        [{"LOWER": "tomorrow"}],
        [{"LOWER": "tmrw"}],
        [{"SHAPE": "dddd-dd-dd"}],
    ]

    # Defined patterns for passenger count
    passenger_count_patterns = [
        [{"LIKE_NUM": True}],
    ]

    matcher.add("PASSENGER_COUNT", passenger_count_patterns)
    matcher.add("GPE", location_patterns)
    matcher.add("DATE", date_patterns)


    for sentence in doc.sents:
        for token in sentence:
            token_dep += str(token.dep_) + " "
            # Check for "day after tomorrow" or "day after tmrw"
            if token.text.lower() == "day" and token.nbor().text.lower() == "after":
                next_token = token.nbor(2)
                if next_token.text.lower() in ["tomorrow", "tmrw"]:
                    date = (datetime.now() + timedelta(days=2)).strftime("%Y/%m/%d")
                    date_set = True
            if token.dep_ in ('cc', 'relcl') and activity_preference is None:
                conj_act_pref_index = token.i
                activity_preference = sentence[conj_act_pref_index:].text

    print(token_dep)
    print("Activity preference phrase is : " + str(activity_preference))

    for ent in doc.ents:
        token_labels += str(ent.label_) + " "
        # Identify location and date based on named entity recognition (NER)
        if ent.label_ == "GPE" and location is None:
            location = ent.text
        elif ent.label_ == "DATE" and date is None and date_set is False:
            date = ent.text
        elif ent.label_ == "PASSENGER_COUNT" and friend_count is None:
            friend_count = ent.text

    if location is None or (date is None and date_set is False) or friend_count is None:
        matches = matcher(doc)
        date_patterns = r'(th|nd|rd|st)$'
        for match_id, start, end in matches:
            string_id = nlp.vocab.strings[match_id]
            span = doc[start:end]
            if doc.vocab.strings[match_id] == "GPE":
                location = span.text
            if doc.vocab.strings[match_id] == "DATE" and date_set is False:
                date = span.text
            if doc.vocab.strings[match_id] == "PASSENGER_COUNT" and not(re.search(date_patterns, span.text)):
                friend_count = span.text

    print("Location is : " + str(location))
    print("Date is : " + str(date))
    print("Passenger Count is : " + str(friend_count))
    print("\n")
    if date_set is False:
        if date is None:
            date = datetime.now().strftime("%Y/%m/%d")
        else:
            date = date_identifier(str(date))
    return location,date,activity_preference


def date_identifier(date_prompt):
    cal = pdt.Calendar()
    now = datetime.now()

    # Remove extra words in date
    words_to_remove = ["in", "the", "of"]
    pattern = r'\b(?:{})\b'.format('|'.join(map(re.escape, words_to_remove)))
    date_string = re.sub(pattern, '', date_prompt, flags=re.IGNORECASE)

    # Calculate date
    if "tmrw" in date_string.lower():
        return (now + timedelta(days=1)).strftime("%Y/%m/%d")
    else:
        dt = cal.parseDT(date_string, now)[0]
        formatted_date = dt.strftime("%Y/%m/%d")
        print(f"The date is - {date_string}: {formatted_date}")
        print("\n")
        return formatted_date