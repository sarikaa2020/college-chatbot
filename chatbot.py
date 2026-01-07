import json
import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download("punkt")
nltk.download("stopwords")

stop_words = set(stopwords.words("english"))

with open("intents.json") as file:
    data = json.load(file)

def clean_sentence(sentence):
    words = word_tokenize(sentence.lower())
    return [w for w in words if w.isalnum() and w not in stop_words]

def similarity(a, b):
    a = set(a)
    b = set(b)
    return len(a & b) / max(len(a | b), 1)

def get_response(user_input):
    user_words = clean_sentence(user_input)

    best_score = 0
    best_response = None

    for intent in data["intents"]:
        if intent["tag"] == "fallback":
            continue

        for pattern in intent["patterns"]:
            pattern_words = clean_sentence(pattern)
            score = similarity(user_words, pattern_words)

            if score > best_score:
                best_score = score
                best_response = random.choice(intent["responses"])

    # THRESHOLD (VERY IMPORTANT)
    if best_score < 0.3:
        # return fallback
        for intent in data["intents"]:
            if intent["tag"] == "fallback":
                return random.choice(intent["responses"])

    return best_response
