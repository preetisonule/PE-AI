import json
import random
import pickle
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

nltk.download('punkt')

# Load intents
with open('intents.json') as f:
    data = json.load(f)

# Prepare training data
corpus = []
labels = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        corpus.append(pattern)
        labels.append(intent['tag'])

# Vectorize text
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)

# Train model
model = MultinomialNB()
model.fit(X, labels)

# Save model + vectorizer
with open('chat_model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

print("✅ Model trained and saved successfully!")
