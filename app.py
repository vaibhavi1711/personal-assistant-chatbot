from flask import Flask, render_template, request, jsonify
from chatbot import bot
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_message = request.json.get("message")
    
    # Handle dynamic time request
    if "time" in user_message.lower():
        return jsonify({"response": f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}"})
    
    response = bot.get_response(user_message)
    return jsonify({"response": str(response)})

if __name__ == "__main__":
    app.run(debug=True)
