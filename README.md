# Simple Rule-Based Chatbot

A basic chatbot built in Python that responds to greetings and common questions using keyword matching.

## How it works
- User input is matched against a set of predefined keywords (`hello`, `how are you`, `your name`, `help`, `weather`, `thanks`, `bye`, etc.)
- If a keyword is found in the input, the bot picks a random matching response.
- If no keyword matches, it returns a fallback message.
- Typing `bye`, `quit`, or `exit` ends the conversation.

## How to run
```bash
python3 chatbot.py
```

## Example
ChatBot: Hi! I'm a simple chatbot. Type 'bye' or 'quit' to exit.
You: hello
ChatBot: Hey, how's it going?
You: what's your name
ChatBot: I'm ChatBot, your friendly rule-based assistant.
You: bye
ChatBot: Goodbye! Have a great day!
