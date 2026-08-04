"""
Simple Rule-Based Chatbot
Responds to greetings, common questions, and exits on a quit command.
"""

import random

# Keyword : list of possible responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey, how's it going?"],
    "hi": ["Hey!", "Hi! How can I help you today?"],
    "how are you": ["I'm just a bunch of code, but I'm doing great!", "Doing well, thanks for asking!"],
    "your name": ["I'm ChatBot, your friendly rule-based assistant.", "You can call me ChatBot."],
    "help": ["I can chat about greetings, how you're doing, or just keep you company. Try saying 'bye' to exit."],
    "weather": ["I can't check live weather, but I hope it's nice where you are!"],
    "thank you": ["You're welcome!", "Anytime!"],
    "thanks": ["No problem!", "Glad I could help!"],
    "bye": ["Goodbye! Have a great day!", "See you later!"],
}

# Keywords that end the conversation
exit_commands = {"bye", "quit", "exit"}


def get_response(user_input):
    """
    Match user input against known keywords and return an appropriate response.
    If no keyword matches, return a default fallback response.
    """
    user_input = user_input.lower().strip()

    for keyword, reply_list in responses.items():
        if keyword in user_input:
            return random.choice(reply_list)

    return "Sorry, I didn't understand that. Could you rephrase?"


def chat():
    """Main loop: reads user input, matches it, and replies until user quits."""
    print("ChatBot: Hi! I'm a simple chatbot. Type 'bye' or 'quit' to exit.")

    while True:
        user_input = input("You: ")

        if user_input.lower().strip() in exit_commands:
            print("ChatBot:", get_response(user_input))
            break

        print("ChatBot:", get_response(user_input))


if __name__ == "__main__":
    chat()
