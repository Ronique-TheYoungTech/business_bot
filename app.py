from flask import Flask, render_template, request, jsonify
from chatbot_logic.chatbot_logic  import get_response  # Correct import path

# Initialize Flask app
app = Flask(__name__)

# Route for the main page
@app.route("/")
def index():
    return render_template("index.html")

# Route for chatbot responses
@app.route("/chat", methods=["POST"])
def chat():
    # Get the user's message from the front-end
    user_message = request.json.get("message", "")
    
    # Process the user's message through the chatbot logic
    bot_response = get_response(user_message)
    
    # Return the chatbot's response to the front-end
    return jsonify({"response": bot_response})

# Run the app
if __name__ == "__main__":
    app.run(debug=True)

import os
print("Current Working Directory:", os.getcwd())
print("chatbot_logic Path Exists:", os.path.exists("chatbot_logic"))

