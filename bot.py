import telebot
import requests
import random

tok = '7202104518:AAFeZK4Dz9GclJKV0kXOG1Vr9jY3BhPazzU'
#هنا خلي توكن بوتك

bot = telebot.TeleBot(tok)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! أرسل لي الرابط الذي تريد الرشق إليه.")
    
@bot.message_handler(func=lambda message: True)
def handle_link(message):
    link = message.text
    bot.reply_to(message, "جاري معالجة الرابط...")
    
    usr = 'qwertyuiopasdfghjklzxcvbnm'
    m = 0
    for _ in range(10):
        rnd = str("".join(random.choice(usr) for _ in range(6)))
        linkk = link + '?' + rnd
        data = {
            "key": "9ebf8fc4c3a0db827dfe41ac19c545c7",
            "action": "add",
            "service": "12505",
            "link": linkk,
            "quantity": "100"
        }
        m += 100
        url = "https://kd1s.com/api/v2"
        try:
            orde = requests.post(url, data=data).json()
            order = orde["order"]
            bot.send_message(message.chat.id, f"Order : {order}\nNumber : {m}\nlink : {link}\nBY : @PY_50")
        except Exception as e:
            print(e)
            bot.send_message(message.chat.id, f"Message_Error{str(e)}")
            break

bot.polling()
