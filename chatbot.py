from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import datetime

# Create chatbot
bot = ChatBot('PersonalAssistant', storage_adapter='chatterbot.storage.SQLStorageAdapter')

# Train bot with English corpus
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

# Custom training for personal assistant tasks
custom_trainer = ListTrainer(bot)
custom_trainer.train([
    "Hi",
    "Hello! How can I help you today?",

    "How are you doing?",
    "I am good, thank you!",

    "What is your name?",
    "I am your personal assistant.",

    "Who created you?",
    "I was created using Python and Flask!",

    "Tell me a joke",
    "Why did the computer go to the doctor? Because it caught a virus!",
    
    "What time is it?",
    f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}"
])
