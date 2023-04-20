



# Chat Bot
Chat Bot is a CLI that will have a conversation with you, and specializes in travel. It will tell you about the best hotels, restaurants, and tourist attractions in a given city.
## debug.py
This file contains the city, restaurant, hotel, and tourist attraction data, and adds it to the database.
## chat.py
This file contains predetermined inputs and responses for the chatbot. It has methods that search for hotels, restaurants, and attractions in a city that the user inputs. It uses SQLAlchemy to interact with the database.
## models.py
This file defines the tables of data using SQLAlchemy.