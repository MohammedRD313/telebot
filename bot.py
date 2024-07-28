import telebot
from telebot import types 
import requests
from telebot.types import InlineKeyboardButton as Btn , InlineKeyboardMarkup as Mak
token = "7202104518:AAFeZK4Dz9GclJKV0kXOG1Vr9jY3BhPazzU"
bot = telebot.TeleBot(token)
bot.set_my_commands([telebot.types.BotCommand("/start", "🤖 تشغيل البوت")])

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.InlineKeyboardMarkup()
    
    wevy = types.InlineKeyboardButton("مطور البوت 👨‍🔧", url='https://t.me/PY_50')
    wev = types.InlineKeyboardButton("قناتي", url='https://t.me/ttxxxn')
    markup.add(wevy,wev)
    name = message.from_user.first_name
    bot.reply_to(message,f'''<b>مرحباً {name}
-! في بـوت تحميل من تيكـتوك ارسـل
الان رابـط لتحميل من فضلك .</b>''',parse_mode='HTML',reply_markup=markup)
	
@bot.message_handler(func=lambda brok:True)
def Url(message):
		markup = types.InlineKeyboardMarkup()
    
		wev = types.InlineKeyboardButton("تم التحميل بواسطه", url='https://t.me/ttxxxn')
		markup.add(wev)
		try:
			msgg = bot.send_message(message.chat.id, "*جاري التحميل ...*",parse_mode="markdown")
			msg = message.text
			url = requests.get(f'https://tikwm.com/api/?url={msg}').json()
			music = url['data']['music']
			region = url['data']['region']
			tit = url['data']['title']
			vid = url['data']['play']
			ava = url['data']['author']['avatar']
			##
			name = url['data']['music_info']['author']
			time = url['data']['duration']
			sh = url['data']['share_count']
			com = url['data']['comment_count']
			wat = url['data']['play_count']
			bot.delete_message(chat_id=message.chat.id, message_id=msgg.message_id)
			bot.send_photo(message.chat.id,ava,caption=f'- اسم الحساب : *{name}*\n - دوله الحساب : *{region}*\n\n- عدد مرات المشاهدة : *{wat}*\n- عدد التعليقات : *{com}*\n- عدد مرات المشاركة : *{sh}*\n- طول الفيديو : *{time}*',parse_mode="markdown")

			bot.send_video(message.chat.id,vid, caption=f"{tit}",reply_markup=markup)
		except:
			pass
			bot.delete_message(chat_id=message.chat.id, message_id=msgg.message_id)
			bot.reply_to(message,'error );')


print('run')
bot.infinity_polling()
