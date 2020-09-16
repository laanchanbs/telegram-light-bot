! pip install adafruit-io

X = os.getenv('X')
Y = os.getenv('Y')

from Adafruit_IO import Client, Feed
aio = Client(X,Y)


!pip install python-telegram-bot

from telegram.ext import Updater,CommandHandler, MessageHandler, Filters  

import requests  # Getting the data from the cloud


def lightoff(bot,update):
    data = aio.send('lightbot', 0)
    rdata = aio.receive('lightbot').value
    chat_id = bot.message.chat_id
    bot.message.reply_text('Okay. Turning off the light')
    update.bot.sendPhoto(chat_id=chat_id, photo="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQ8jpdHR_pFaoP2Vudl7k-46mSK7I3shuCvFw&usqp=CAU", caption="Light off")
    
def lighton(bot,update):
    data = aio.send('lightbot', 1)
    rdata = aio.receive('lightbot').value
    chat_id = bot.message.chat_id
    bot.message.reply_text('Okay. Turning on the light')
    update.bot.sendPhoto(chat_id=chat_id, photo="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRgKuBghXuR_IjPXnRu9o2znn0O_avidTs-ig&usqp=CAU", caption="Light on")
   
def chooser(bot,update):
          chat_id = bot.message.chat_id
            
          a = bot.message.text

          data = aio.receive_previous('lightbot')
            
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

def main():
  BOT_TOKEN= '1099855077:AAHy6EhrOwabbIo_XVDO5_FjUGgR14hoeJE'
  u = Updater(BOT_TOKEN, use_context=True)
  dp = u.dispatcher
  dp.add_handler(MessageHandler(Filters.text, chooser))
  u.start_polling()
  u.idle()

if __name__ == '__main__':
    main()
