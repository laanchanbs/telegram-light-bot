! pip install adafruit-io

X = os.getenv('X')
Y = os.getenv('Y')

from Adafruit_IO import Client, Feed
aio = Client(X,Y)

!pip install python-telegram-bot

from telegram.ext import Updater,CommandHandler, MessageHandler, Filters  

import requests  # Getting the data from the cloud

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents ['url']
    return url



def lighton(bot,update):
    data = aio.send('lightbot', 1)
    rdata = aio.receive('lightbot').value
    chat_id = update.message.chat_id
    bot.send_message(chat_id,text='Light is On')
    bot.send_message(chat_id,text='Thank you')


def lightoff(bot,update):
    data = aio.send('lightbot', 0)
    rdata = aio.receive('lightbot').value
    chat_id = update.message.chat_id
    bot.send_message(chat_id,text='Light is Off')
    bot.send_message(chat_id,text='Thank you')
   
def chooser(bot,update):
          chat_id = update.message.chat_id
            
          a = update.message.text
            
          if a == "Light on" or a =="Light ON" or a =="Light On" or a == "LIGHT ON":
                { 
                        lighton(bot,update)
                }
          elif a == "Light off" or a =="Light OFF" or a =="Light Off" or a == "LIGHT OFF" :
                {
                        lightoff(bot,update)
                }
          else:
                {
                        bot.send_message(chat_id,text='Invalid Text')
                }    

u = Updater('1099855077:AAHy6EhrOwabbIo_XVDO5_FjUGgR14hoeJE')
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text, chooser))
u.start_polling()
u.idle()
