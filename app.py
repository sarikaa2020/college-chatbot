from flask import Flask, render_template, request, jsonify
from chatbot import get_response
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# ✅ Welcome message API
@app.route("/welcome", methods=["GET"])
def welcome():
    return jsonify({
        "reply": "👋 Hello! I am the College Chatbot.\n\nAsk me about:\n• Admissions\n• Courses\n• Fees\n• Placements\n• College details"
    })

@app.route("/get", methods=["POST"])
def chat():
    user_msg = request.json["msg"]
    reply = get_response(user_msg)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


