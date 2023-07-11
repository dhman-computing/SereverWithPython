import os
import telebot
# import time
from support import fileLog
from threading import Thread

def run_bot():
    b_tkn = os.environ.get('BOT_TOKEN')
    # print(b_tkn)

    bot = telebot.TeleBot(b_tkn)

    
    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        print(f"#{message.id} Message Rcieved from User {message.from_user.id}.")
        reply = "Howdy, how are you doing?"
        # print(6)
        fileLog(reply, message)
        # print(5)
        bot.reply_to(message, reply)

    @bot.message_handler(commands=['url'])
    def send_url(message):
        print(f"#{message.id} Message Rcieved from User {message.from_user.id}.")
        reply = "https://serverwithpython.dhimancomputing.repl.co"
        # print(7)
        fileLog(reply, message)
        # print(8)
        bot.reply_to(message, reply)
    
    @bot.message_handler(func=lambda message: True)
    def reply(message):
        print(f"#{message.id} Message Rcieved from User {message.from_user.id}.")
        if message.text == "Dhiman":
            reply = "Hello, Boss."
        else:
            # print(3)
            reply = "Message Saved"
            # print(2)
        # print(4)
        fileLog(reply, message)
        # print(1)
        bot.reply_to(message, reply)

    bot.infinity_polling()


def keep_bot_alive():
  t = Thread(target=run_bot)
  t.start()