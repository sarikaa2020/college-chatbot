import json
import random
import nltk
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')

with open("intents.json") as file:
    data = json.load(file)

def get_response(user_input):
    sentences = []
    tags = []

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            sentences.append(pattern)
            tags.append(intent)

    sentences.append(user_input)

    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(sentences)

    similarity = cosine_similarity(vectors[-1], vectors[:-1])
    best_match = similarity.max()

    # ✅ Fallback condition
    if best_match < 0.2:
        return "❌ Sorry, I didn’t understand that.\nPlease ask about admissions, courses, fees, or placements."

    index = similarity.argmax()
    intent = tags[index]

    return random.choice(intent["responses"])
