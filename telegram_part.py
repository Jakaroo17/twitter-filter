
import hashlib
import telebot
from config import TELEGRAM_API_TOKEN as TAT
hash = '35ebeaecf742b21016912ccd0f9e23d8'
bot = telebot.TeleBot(TAT)

@bot.message_handler(commands = ['start'])
def start_msg(message):
    bot.reply_to(message,"Аутифенцируйся")
    auth()


@bot.message_handler(content_types=['text'])
def auth(message):
    print(message.text)
    print(hashlib.md5(message.text.encode('utf-8')).hexdigest())
    if hashlib.md5(message.text.encode('utf-8')).hexdigest() == hash:
        bot.reply_to(message,'Good')
    else:
        bot.reply_to(message,'not good')

bot.polling()
# text = str(input()).encode('utf-8')
# hash_object = hashlib.md5(text).hexdigest()

