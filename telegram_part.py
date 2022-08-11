
from email import message
import hashlib
from pickle import TRUE
import telebot
from config import TELEGRAM_API_TOKEN,ADMIN_HASH 
from filter_method import Filter
from time import sleep
from os.path import join, dirname


bot = telebot.TeleBot(TELEGRAM_API_TOKEN)
twitter_object = None
@bot.message_handler(commands = ['start'])
def start_msg(message):
    bot.reply_to(message,"This bot sets stopwords or language filtration in replies for twitter account. Please insert all API keys or use default configuration if you're admin")
    keyboard = telebot.types.InlineKeyboardMarkup()
    key_admin = telebot.types.InlineKeyboardButton(text="Admin",
                                                    callback_data = "admin_cofig")
    key_new = telebot.types.InlineKeyboardButton(text="New_account",
                                                    callback_data = "new_cofig")
    keyboard.add(key_admin)
    keyboard.add(key_new)
    bot.send_message(message.from_user.id,text="Admin or new user?",reply_markup=keyboard)

@bot.message_handler(commands = ['helplang'])
def help_language_list(message):
    data = open(join(dirname(__file__),"langhelp.txt")).readlines()
    str = ""
    for x in data:
        str += x
    bot.send_message(message.chat.id,str)
    

@bot.callback_query_handler(func=lambda call: True)
def auth(call):
    if call.data == "Admin":
        bot.send_message(call.message.chat.id,'Enter Admin Password')
        AdminPassword = call.message
        print(AdminPassword)


    elif (call.data == "New"):
        pass
    


flag = 1
@bot.message_handler(commands=['startloop'])
def loop(msg):
    a = 0
    global flag
    flag = 1 
    if not twitter_object:
        bot.send_message(msg.chat.id,"You need to auth first")
    while flag and not twitter_object:
        a+=1
        print(a)
        bot.send_message(msg.chat.id, "ping")
        sleep(100)

@bot.message_handler(commands=['stop', 'end'])
def stop(msg):
    global flag
    flag = 0
    bot.send_message(msg.chat.id, "stopped")




bot.polling()
    

