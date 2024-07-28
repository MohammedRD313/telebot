from telebot import *
from mindai import *
from types import *
bot = TeleBot("7202104518:AAFeZK4Dz9GclJKV0kXOG1Vr9jY3BhPazzU")
#توكن بوتك 
@bot.message_handler(commands=['start'])
def start(message):
    userm = message.from_user.username
    ID = message.from_user.id
    name_pro = message.from_user
    key = types.InlineKeyboardMarkup()
    bot1 = types.InlineKeyboardButton('- Dev 💣' ,url ='https://t.me/Class_zaid')
    bot2 = types.InlineKeyboardButton('- Channel 🔥' ,url ='https://t.me/ZeusThon')
    key.add(bot1,bot2)
    p1ng = "https://t.me/ZeusThon/7038"
    bot.send_photo(message.chat.id,p1ng,f"""<strong>
 English :- 
- Welcom @{userm} .
- Yuor Id {ID}
- Send Yuo And Bot .
- Start Now .
* - - - - - - - - - - - - - - - - -*
Arbic :  
- اهلا بك عزيزي @{userm}💣
تحدث مع البوت بلغه الانكليزي فقط 
ابدء الان .
</strong>""",parse_mode="html",reply_markup=key)
@bot.message_handler(func=lambda message: True)
def main(message):
    x = Ai().chat(message=message.text)
    bot.reply_to(message,x['reply'])
bot.infinity_polling()