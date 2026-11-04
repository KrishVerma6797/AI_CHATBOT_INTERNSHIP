
"""
Simple Rule-Based Chatbot
-------------------------
A terminal chatbot that uses predefined rules, regular expressions,
keyword matching, and intent-based responses.

Requirements: Python 3.10+
External dependencies: None
Run: python chatbot.py
"""

import random
import re
from datetime import datetime


# Predefined intents, patterns, and responses
INTENTS = {
    "greeting": {
        "patterns": [
            r"\b(hi|hello|hey|hii|namaste)\b",
            r"\bgood\s+(morning|afternoon|evening)\b",
        ],
        "responses": [
            "Hello! How can I help you?",
            "Hey! Nice to meet you.",
            "Hi there! What would you like to talk about?",
        ],
    },
    "goodbye": {
        "patterns": [
            r"\b(bye|goodbye|exit|quit|see you|see ya)\b",
        ],
        "responses": [
            "Goodbye! Have a great day!",
            "See you soon. Take care!",
            "Thanks for chatting. Bye!",
        ],
    },
    "thanks": {
        "patterns": [
            r"\b(thanks|thank you|thx|thankyou)\b",
        ],
        "responses": [
            "You're welcome!",
            "Happy to help!",
            "Anytime! Let me know if you need anything else.",
        ],
    },
    "name": {
        "patterns": [
            r"\bwhat is your name\b",
            r"\bwho are you\b",
            r"\byour name\b",
        ],
        "responses": [
            "I'm RuleBot, a simple rule-based chatbot.",
            "You can call me RuleBot!",
        ],
    },
    "feeling": {
        "patterns": [
            r"\bhow are you\b",
            r"\bhow are you doing\b",
            r"\bhow do you feel\b",
        ],
        "responses": [
            "I'm doing great! Thanks for asking.",
            "I'm ready to chat. How are you?",
        ],
    },
    "help": {
        "patterns": [
            r"\bhelp\b",
            r"\bwhat can you do\b",
            r"\bhow can you help\b",
        ],
        "responses": [
            "I can greet you, tell you my name, share the date and time, "
            "and respond to simple questions. Try asking me something!"
        ],
    },
    "time": {
        "patterns": [
            r"\bwhat time is it\b",
            r"\bcurrent time\b",
            r"\btell me the time\b",
        ],
        "responses": [],
    },
    "date": {
        "patterns": [
            r"\bwhat is the date\b",
            r"\bcurrent date\b",
            r"\btoday'?s date\b",
            r"\bwhat day is it\b",
        ],
        "responses": [],
    },
    "creator": {
        "patterns": [
            r"\bwho created you\b",
            r"\bwho made you\b",
            r"\bwho is your creator\b",
        ],
        "responses": [
            "I was created using Python and predefined rules.",
            "A Python programmer built me using patterns and conditions.",
        ],
    },
    "joke": {
        "patterns": [
            r"\btell me a joke\b",
            r"\bmake me laugh\b",
            r"\bsomething funny\b",
        ],
        "responses": [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why was the computer cold? It left its Windows open!",
            "Why did the Python programmer wear glasses? To improve their C#!",
        ],
    },
}

FALLBACK_RESPONSES = [
    "I'm not sure I understand. Could you rephrase that?",
    "Interesting! Can you tell me a little more?",
    "I don't have a rule for that yet. Try asking something else.",
]

# Words and phrases are normalized before matching.
NON_WORD_PATTERN = re.compile(r"[^\w\s']", flags=re.UNICODE)


def clean_text(text: str) -> str:
    """Normalize input by lowercasing and removing extra punctuation."""
    text = text.lower().strip()
    text = NON_WORD_PATTERN.sub(" ", text)
    return re.sub(r"\s+", " ", text)


def detect_intent(message: str) -> str | None:
    """Identify the first matching intent using regular expressions."""
    for intent, details in INTENTS.items():
        for pattern in details["patterns"]:
            if re.search(pattern, message):
                return intent
    return None


def generate_response(intent: str | None) -> str:
    """Generate a response according to the detected intent."""
    now = datetime.now()

    if intent == "time":
        return f"The current time is {now.strftime('%I:%M %p')}."

    if intent == "date":
        return f"Today's date is {now.strftime('%d %B %Y')}."

    if intent in INTENTS:
        responses = INTENTS[intent]["responses"]
        if responses:
            return random.choice(responses)

    return random.choice(FALLBACK_RESPONSES)


def chatbot() -> None:
    """Run the chatbot's interactive terminal conversation."""
    print("=" * 45)
    print("       Welcome to RuleBot!")
    print("=" * 45)
    print("Type 'help' to see what I can do.")
    print("Type 'bye' or 'exit' to end the conversation.\n")

    while True:
        try:
            user_input = input("You: ").strip()

            if not user_input:
                print("RuleBot: Please enter a message.\n")
                continue

            message = clean_text(user_input)

            if not message:
                print("RuleBot: Please enter a meaningful message.\n")
                continue

            intent = detect_intent(message)
            response = generate_response(intent)

            print(f"RuleBot: {response}\n")

            if intent == "goodbye":
                break

        except (KeyboardInterrupt, EOFError):
            print("\nRuleBot: Goodbye! Thanks for chatting.")
            break


if __name__ == "__main__":
    chatbot()
