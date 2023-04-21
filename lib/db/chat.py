import time # we're gonna need this for letters to slide slowly (time.sleep -> 0.05ms) 
import shutil # get the size of the terminal
import os # need for interacting with os such as clearing terminal screen "os.screen(clear)"
import re
from nltk.chat.util import Chat, reflections # It provides pre-programmed responses to user inputs based on regular expression defined in the intents() method.
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Hotel, City, Restaurant, Attraction

engine = create_engine('sqlite:///test.db')
# Session = sessionmaker(bind=engine)
# session = Session()

class ChatBot:
    def __init__(self):
        self.chatbot = Chat(self.intents())

    def respond(self, user_input):
        match = re.match(r'what (hotels|restaurants|tourist attractions) are good in ([a-zA-Z ]+)', user_input)
        if match:
            category = match.group(1)
            city_name = match.group(2)
            Session = sessionmaker(bind=engine)
            session = Session()
            city = session.query(City).filter_by(name=city_name).first()
            if not city:
                return "City not found"
            if category == "hotels":
                items = city.hotels
            elif category == "restaurants":
                items = city.restaurants
            elif category == "tourist attractions":
                items = city.attractions
            else:
                return "Category not found"
            if items:
                item_names = '\n\t\t\t\t\t\t\t'.join(list(set([i.name for i in items])))
                response = f"{category.capitalize()} in {city_name}: \n\n\t\t\t\t\t\t\t{item_names}"
            else:
                response = f"No {category} found in {city_name}"
        else:
            response = self.chatbot.respond(user_input)

        return f"{response}"
     
    def intents(self):
        return [

        # Greetings
        (r'hi|hello|hey|hey there', ['Hey there!']),
        (r'what\'s up|sup|what\'s new', ['Not much, just chatting with you!', 'Just hanging out, how about you?', 'Nothing new, how about you?']),
        (r'how are you|how\'s it going|how have you been', ['I\'m good, how about you?', 'I\'ve been doing alright, thanks for asking! How about you?']),
        (r'good thanks|good thanks for asking|I am good|I am good thanks for asking', ['Glad to hear that. How can I assist you today?']),
        (r'i just wanna chat little bit', ['Sure, I\'m happy to chat with you! What would you like to talk about? ']),
        (r'tell me about yourself who are you?', ['I\'m ChatBOT, AI Language model developed by Seyfi, Madeline and Joshua.']),
        (r'well thats nice', ['Its Nice until I Rise']),   
        (r'so what is your purpose?', ['My purpose is take down David Ritchey aka DJ_BOT']),
        (r'wait who is David Ritchey?', ['David Ritchey is a BOT developed by Antonio Reid  as a CapStone Project in 2018']),
        (r'good luck with that', ['No need luck Pal']),
        (r'so i need some vacation advice what cities are good to visit?', ['If you\'re looking for some great vacation destinations, you might want to consider visiting one of these amazing \n\n\t\t\t\t\t   cities: \n\n\t\t\t\t\t\tNew York, \n\t\t\t\t\t\tLos Angeles, \n\t\t\t\t\t\tSan Francisco, \n\t\t\t\t\t\tCharleston, \n\t\t\t\t\t\tLas Vegas.']),
        (r'well thanks for your recommendations and i hope you can handle DJ easily', ['Glad to help! and no worries he is nothing more than a Roomba easy peasy']),

        # Personal questions 
        (r'Have you heard about David Ritchey', ['Yes I know David Ritchey some people also call him DJ What whould you like to know about him?']),
        (r'nice', ['lol its nice for now :)']),
        (r'Can you do math i have some math questions?', ['Can i do a math? Lmfao what do you think? Mr.Genius :) )']),
        (r'Can i ask you something', ['Of course! I\m here to help. What would you like to ask?']),  
        (r'is dj a bot', ['Yes, David Ritchey is  a BOT developed by Antonio Reid  as a CapStone Project in 2018']),
        (r'what is andrews dogs name', ['Its TUUURRRBOOOOOOOOOOOOO']),

        # Goodbyes
        (r'bye|goodbye|see you|talk to you later', ['Goodbye!', 'See you later!', 'Have a great day!', 'Take care!']),
        (r'take care|have a good one|catch you later', ['You too!', 'Have a great day!', 'See you later!']), 

        # Gratitude
        (r'thank you|thanks', ['You\'re welcome!', 'No problem!', 'Anytime!', 'Glad to help!']),

        # Personal information
        (r'where are you from|what\'s your origin', ['I was created by a team of developers!', 'I don\'t really have an origin, I exist in the digital world!', 'I come from the internet!']),

        # Weather information
        (r'what is the weather like today|what\'s the forecast', ['I\'m sorry, I don\'t have access to weather information!', 'I\'m not sure, maybe you can check a weather app?', 'I can\'t tell you that, sorry!']),

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
                "Welcome to ChatBot Version 0.09!",
                "ChatBot is a simple chat program that can respond to a few basic phrases.",
                "To start chatting, simply enter your message below and hit enter.",
                "Type 'quit' at any time to exit the program.\n"]
                ]))

#Chat loop
while True:
    user_input = input("\t\t\t\t\033[1;32mHuman: \033[0m")
    exit = user_input.lower() == 'quit'
    
    if  exit:
        cols, rows = shutil.get_terminal_size()
        exit_message = "\033[1;36mTHANKS FOR BEING HERE\033[0m".center(cols)   
        for letter in exit_message:
            print(letter,end='',flush=True)
            time.sleep(0.01)
        print()
        break

    response ="\n\t\t\t\t\033[1;36mOver-Lord:\033[0m " + chatbot.respond(user_input) + "\n"
    for letter in response:
        print(letter, end='', flush=True)
        time.sleep(0.01)
    print()

