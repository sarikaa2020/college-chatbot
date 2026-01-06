import json
import random
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')

with open("intents.json") as file:
    data = json.load(file)

patterns = []
responses = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        patterns.append(pattern)
        responses.append(random.choice(intent["responses"]))

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(patterns)

def get_response(user_input):
    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, X)
    index = similarity.argmax()
    return responses[index]

