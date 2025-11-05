# hii
from flask import Flask, render_template, request, jsonify
import random, pickle, json

app = Flask(__name__)

# Load model, vectorizer, and intents
model = pickle.load(open('chat_model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
intents = json.load(open('intents.json'))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chat():
    user_msg = request.form["msg"]
    X = vectorizer.transform([user_msg])
    intent_tag = model.predict(X)[0]

    for intent in intents["intents"]:
        if intent["tag"] == intent_tag:
            response = random.choice(intent["responses"])
            break

    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
