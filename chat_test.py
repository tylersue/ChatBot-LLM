import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you', ['I\'m doing well, thank you!', 'I\'m fine, how about you?']),
    (r'what is your name', ['My name is ChatBot.', 'I\'m ChatBot, nice to meet you!']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Take care!']),
    (r'what can you do', ['I can chat with you on various topics!', 'I\'m here to assist you with information and conversation.']),
    (r'tell me a joke', ['Why don\'t scientists trust atoms? Because they make up everything!', 'What do you call a fake noodle? An impasta!']),
    (r'who created you', ['I was created by a team of developers.', 'I\'m an AI chatbot, created by programmers.']),
    (r'what\'s the weather like', ['I\'m sorry, I don\'t have access to real-time weather information.', 'You might want to check a weather app or website for that information.']),
    (r'thank you', ['You\'re welcome!', 'Glad I could help!', 'My pleasure!']),
    (r'how old are you', ['As an AI, I don\'t have an age in the traditional sense.', 'I\'m a computer program, so I don\'t age like humans do.']),
    (r'favorite (color|colour)', ['As an AI, I don\'t have personal preferences, but I find all colors fascinating!']),
    (r'do you have feelings', ['As an AI, I don\'t have feelings in the way humans do. I\'m designed to process information and respond accordingly.']),
    (r'what\'s the meaning of life', ['That\'s a profound question! Philosophers have debated it for centuries. What do you think?']),
    (r'can you learn', ['While I can\'t learn in real-time, my knowledge is regularly updated by my developers.']),
    (r'what languages do you speak', ['I\'m primarily designed to communicate in English, but I can understand and process many languages.']),
    (r'are you intelligent', ['I\'m an artificial intelligence, designed to process and respond to a wide range of inputs. But intelligence is a complex concept!']),
    (r'(.*)', ['I\'m not sure how to respond to that.', 'Can you please rephrase that?']),
]

# Add more patterns



# Create a Chat object
chatbot = Chat(patterns, reflections)

# ... Implement chatbot logic
# Function to process user input
def process_input(user_input):
    return chatbot.respond(user_input)

# Function to generate response
def generate_response(user_input):
    response = process_input(user_input)
    return response

# Main chatbot loop
def chat_loop():
    print("ChatBot: Hello! How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("ChatBot: Goodbye!")
            break
        response = generate_response(user_input)
        print("ChatBot:", response)
# Function to start the chat
def start_chat():
    print("Hello! I'm ChatBot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("ChatBot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("ChatBot:", response)

# Run the chatbot
if __name__ == "__main__":
    start_chat()
