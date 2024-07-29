import telebot
import random

# أدخل توكن البوت هنا مباشرة
TOKEN = '7231254366:AAHkHtHowT9Sd5iBVJNTqNMdN51uvLPrGsk'
bot = telebot.TeleBot(TOKEN)

# دالة بسيطة لتوليد ردود عشوائية
def gpt(user_input):
    responses = [
        "هذا مثير جدًا!",
        "كيف يمكنني مساعدتك اليوم؟",
        "أخبرني المزيد.",
        "هذا يبدو رائعًا!",
        "أنا هنا للمساعدة!"
    ]
    return random.choice(responses)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "مرحبا أنا سانكا")

@bot.message_handler(content_types=['text'])
def gptMessage(message):
    resp = gpt(message.text)  # استخدم الدالة gpt لتوليد الرد
    bot.send_message(message.chat.id, f'سانکا: {resp}')

bot.infinity_polling()
