import re
import nltk

# First time you run, uncomment this line once:
# nltk.download('punkt')

from nltk.tokenize import word_tokenize

def preprocess(user_input):
    """
    Basic NLP preprocessing:
    - Lowercase
    - Tokenize into words
    """
    user_input = user_input.lower()
    tokens = word_tokenize(user_input)
    return tokens

def chatbot():
    print("Hello! I am your NLP chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Bot: Goodbye! Have a nice day!")
            break

        tokens = preprocess(user_input)

        # -----------------------------
        # Greeting intent
        # -----------------------------
        greeting_words = ["hi", "hello", "hey"]
        is_greeting = False
        for word in tokens:
            if word in greeting_words:
                is_greeting = True
                break

        if is_greeting:
            print("Bot: Hello there! How are you?")
            continue  # skip other checks

        # -----------------------------
        # How are you intent
        # -----------------------------
        if re.search(r"how are you", user_input.lower()):
            print("Bot: I'm doing great, thank you for asking!")
            continue

        # -----------------------------
        # Name intent
        # -----------------------------
        if re.search(r"(your name|who are you)", user_input.lower()):
            print("Bot: I'm a simple NLP-powered chatbot!")
            continue

        # -----------------------------
        # Feeling good intent
        # -----------------------------
        feeling_words = ["good", "great", "fine", "happy"]
        is_feeling_good = False
        for word in tokens:
            if word in feeling_words:
                is_feeling_good = True
                break

        if is_feeling_good:
            print("Bot: That's awesome to hear!")
            continue

        # -----------------------------
        # Help intent
        # -----------------------------
        is_help = False
        for word in tokens:
            if word == "help":
                is_help = True
                break

        if is_help:
            print("Bot: You can ask me about my name, how I feel, or just say hello.")
            continue

        # -----------------------------
        # Unknown intent
        # -----------------------------
        print("Bot: Hmm, I didn’t quite understand. Can you try rephrasing?")

if __name__ == "__main__":
    chatbot()
