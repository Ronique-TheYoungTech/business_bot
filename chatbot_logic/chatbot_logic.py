import sqlite3
import random

def get_response(user_message):
    """
    Get a response from the database or provide a conversational fallback.
    """
    # Connect to the database
    connection = sqlite3.connect("faq.db")
    cursor = connection.cursor()

    # Try to match the user's question with one in the database
    query = "SELECT answer FROM faq WHERE question = ?"
    cursor.execute(query, (user_message,))
    result = cursor.fetchone()

    # Close the connection
    connection.close()

    # If a response is found in the database
    if result:
        return result[0]  # Return the answer from the database

    # If no response is found, provide a conversational fallback
    else:
        return handle_fallback(user_message)


def handle_fallback(user_message):
    """
    Provide a fallback response when the user's message doesn't match known data.
    """
    general_fallbacks = [
        "That's an interesting question. Could you tell me more?",
        "Hmm, I don't have an answer for that right now, but I'm learning!",
        "I'm not sure about that. Can you rephrase your question?",
        "Sorry, I didn't get that. Let's try again!",
    ]

    # Add a little variety to the responses
    fallback_response = random.choice(general_fallbacks)

    # If the user greets the bot
    if any(greeting in user_message.lower() for greeting in ["hi", "hello", "hey"]):
        return "Hello! How can I help you today?"

    # If the user thanks the bot
    elif "thank" in user_message.lower():
        return "You're welcome! Is there anything else I can help you with?"

    # If the user says goodbye
    elif any(farewell in user_message.lower() for farewell in ["bye", "goodbye", "see you"]):
        return "Goodbye! Have a great day!"

    # Default fallback response
    return fallback_response


# Test the chatbot logic
if __name__ == "_main_":
    print("Chatbot: Hi there! Ask me anything or type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        bot_response = get_response(user_input)
        print(f"Chatbot: {bot_response}")