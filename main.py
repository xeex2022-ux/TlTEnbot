import telebot, os
from flask import Flask
from threading import Thread

TOKEN=os.environ.get("BOT_TOKEN")
bot=telebot.TeleBot(TOKEN)
app=Flask(__name__)

@bot.message_handler(commands=['start'])
def s(m): bot.reply_to(m,"شغال ✅")

@bot.message_handler(func=lambda m:True)
def a(m): bot.reply_to(m,m.text)

@app.route('/')
def h(): return "OK"

def run(): bot.infinity_polling()

Thread(target=run).start()
app.run(host="0.0.0.0",port=int(os.environ.get("PORT",10000)))
