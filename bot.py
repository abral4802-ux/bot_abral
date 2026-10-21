import telebot
from telebot import types
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("💰 HARGA","👤 OWNER","⭐ TESTI")
    bot.send_message(m.chat.id, "🔥 ABRAL STORE 🔥\n\nOwner @abral09\n\nPilih menu dibawah wok:", reply_markup=kb)

@bot.message_handler(func=lambda m: m.text == "💰 HARGA")
def harga(m):
    bot.send_message(m.chat.id, "💰 LIST HARGA:\n\nBUG WA 5K\nUNBAND WA 10K")

@bot.message_handler(func=lambda m: m.text == "👤 OWNER")
def owner(m):
    mk = types.InlineKeyboardMarkup()
    mk.add(types.InlineKeyboardButton("Chat @abral09", url="https://t.me/abral09"))
    bot.send_message(m.chat.id, "Owner @abral09", reply_markup=mk)

@bot.message_handler(func=lambda m: m.text == "⭐ TESTI")
def testi(m):
    mk = types.InlineKeyboardMarkup()
    mk.add(types.InlineKeyboardButton("LIHAT TESTI", url="https://whatsapp.com/channel/0029VbE0Lm7EAKWAjqBDv33o"))
    bot.send_message(m.chat.id, "Testimoni klik dibawah!", reply_markup=mk)

bot.infinity_polling()
