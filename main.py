import os
import telebot
import json
from random import choice

API_TOKEN = os.getenv("API_TOKEN")

bot = telebot.TeleBot(API_TOKEN)


def get_zekr_sabah(message):
    if "أذكار الصباح" == message.text or "اذكار الصباح" == message.text:
        return True
    else:
        return False


@bot.message_handler(func=get_zekr_sabah)
def azkar_sabah(message):
    with open('azkar.json', encoding='utf-8') as f:
        data = json.load(f)
        for doaa in data:
            if doaa['category'] == "أذكار الصباح":
                bot.send_message(message.chat.id, doaa['zekr'])


def get_zekr_masaa(message):
    if "أذكار المساء" == message.text or "اذكار المساء" == message.text:
        return True
    else:
        return False


@bot.message_handler(func=get_zekr_masaa)
def azkar_sabah(message):
    with open('azkar.json', encoding='utf-8') as f:
        data = json.load(f)
        for doaa in data:
            if doaa['category'] == "أذكار المساء":
                bot.send_message(message.chat.id, doaa['zekr'])


def get_zekr(message):
    if message.text in "ذكر" or message.text in "ذكر":
        return True
    else:
        return False


@bot.message_handler(func=get_zekr)
def azkar(message):
    with open('azkar.json', encoding='utf-8') as f:
        data = json.load(f)
        bot.send_message(message.chat.id, choice(data)['zekr'])


bot.polling()
