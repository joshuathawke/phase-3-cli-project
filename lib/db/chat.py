import time # we're gonna need this for letters to slide slowly (time.sleep -> 0.05ms) 
import shutil # get the size of the terminal
import os # need for interacting with os such as clearing terminal screen "os.screen(clear)"
from nltk.chat.util import Chat, reflections # It provides pre-programmed responses to user inputs based on regular expression defined in the intents() method.

class ChatBot:
    def __init__(self):
        self.chatbot = Chat(self.intents())

    def respond(self, user_input):
        response = self.chatbot.respond(user_input)
        return response


    def intents(self):
        return [
        # Greetings
        (r'hi|hello|hey|howdy|hey there', ['Hello!', 'Hi!', 'Hey there!', 'Howdy!']),
        (r'what\'s up|sup|what\'s new', ['Not much, just chatting with you!', 'Just hanging out, how about you?', 'Nothing new, how about you?']),
        (r'how are you|how\'s it going|how have you been', ['I\'m doing well, thanks for asking!', 'I\'m good, how about you?', 'I\'ve been doing alright, thanks for asking!']),
        
        # Goodbyes
        (r'bye|goodbye|see you|talk to you later', ['Goodbye!', 'See you later!', 'Have a great day!', 'Take care!']),
        (r'take care|have a good one|catch you later', ['You too!', 'Have a great day!', 'See you later!']),

        # Gratitude
        (r'thank you|thanks', ['You\'re welcome!', 'No problem!', 'Anytime!', 'Glad to help!']),

        # Personal information
        (r'what is your name|who are you', ['My name is ChatBot!', 'I\'m an AI chatbot!', 'I\'m ChatBot!', 'You can call me ChatBot!']),
        (r'where are you from|what\'s your origin', ['I was created by a team of developers!', 'I don\'t really have an origin, I exist in the digital world!', 'I come from the internet!']),

        # Weather information
        (r'what is the weather like today|what\'s the forecast', ['I\'m sorry, I don\'t have access to weather information!', 'I\'m not sure, maybe you can check a weather app?', 'I can\'t tell you that, sorry!']),

        ################################################ Personal questions #########################################################
        (r'Have you heard about David Ritchey', ['Yes I know David Ritchey some people also call him DJ What whould you like to know about him?']),
        (r'Can i ask you something', ['Of course! I\m here to help. What would you like to ask?']),  
        (r'is dj a bot', ['Yes, David Ritchey is  a BOT developed by Antonio Reid  as a CapStone Project in 2018']),
        (r'what is andrews dogs name', ['Its TUUURRRBOOOOOOOOOOOOO']),

        # Miscellaneous
        (r'how old are you|when were you created', ['I was created recently!', 'I don\'t have an age, I\'m just a program!', 'I was made by a team of developers!']),
        (r'what can you do|what are your skills', ['I can chat with you and answer your questions!', 'I\'m here to help you with anything you need!', 'I\'m a chatbot, so I can chat with you about anything!']),
        (r'i\'m bored', ['I\'m sorry to hear that! Maybe we can chat and find something to do!', 'Let\'s chat and see if we can come up with something to cure your boredom!']),
        (r'.*', ['I\'m not sure what you mean, can you please rephrase that?', 'Sorry, I don\'t understand what you\'re asking!', 'I\'m not sure I know the answer to that!']),
    ]

chatbot = ChatBot()

## Display the response more clearly and readable
def format_response(response):
    return response.strip()

### Clear terminal and show front page ###
os.system('clear') # clear the terminal when run the program
print("\n".join([line.upper().center(shutil.get_terminal_size().columns) for line in [
                 "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n",
                 "Welcome to ChatBot!",
                 "ChatBot is a simple chat program that can respond to a few basic phrases.",
                 "To start chatting, simply enter your message below and hit enter.",
                 "Type 'quit' at any time to exit the program.\n"]
                 ]))

#Chat loop
while True:
    user_input = input("Human: ")
    exit = user_input.lower() == 'quit'
    
    if  exit:
        exit_message = "\t\t\t\t\t\t\tTHANKS FOR BEING HERE "
        for letter in exit_message:
            print(letter, end='', flush=True)
            time.sleep(0.05)
        print()
        break

    response ="\nOver-Lord: " + chatbot.respond(user_input) + "\n"
    for letter in response:
        print(letter, end='', flush=True)
        time.sleep(0.01)
    print()


