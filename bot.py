import requests, telebot, json
from telebot import types
bot = telebot.TeleBot("7388893810:AAHZwzXl8OQz9A_JAZj5u86Ki7hGP2Vfprk")

'''
My : @ALsultann1
My Ch1 : @radfx2

'''


SS = "dev = @radfx2" 
url = 'https://us-central1-chat-for-chatgpt.cloudfunctions.net/basicUserRequestBeta'

def gpt(text) -> str:
 headers = {
     'Host': 'us-central1-chat-for-chatgpt.cloudfunctions.net',
     'Connection': 'keep-alive',
     'If-None-Match': 'W/"1c3-Up2QpuBs2+QUjJl/C9nteIBUa00"',
     'Accept': '*/*',
     'User-Agent': 'com.tappz.aichat/1.2.2 iPhone/15.6.1 hw/iPhone8_2',
     'Content-Type': 'application/json',
     'Accept-Language': 'en-GB,en;q=0.9'
 }
 
 data = {
     'data': {
         'message':text,
     }
 }

 response = requests.post(url, headers=headers, data=json.dumps(data))
 try:
  result = response.json()["result"]["choices"][0]["text"]
  return result
 except:
  return None 
S = "run bot - المبرمج : @ALsultaNN1"
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    msg = gpt(message.text)
    if msg:
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='- المبرمج .', url="https://t.me/@radfx2"))
        bot.reply_to(message, msg, reply_markup=markup)
    else:
        bot.reply_to(message, "ما فهمت سؤالك ؟")
print(S)
print(SS)
bot.polling()
