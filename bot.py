import telebot
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

# استبدل TOKEN بالتوكن الخاص بالبوت الخاص بك
TOKEN = '7202104518:AAFeZK4Dz9GclJKV0kXOG1Vr9jY3BhPazzU'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🔼 مرحبًا! لإعداد الجلسة، يرجى إدخال APP ID و API HASH.")

@bot.message_handler(func=lambda message: True)
def get_credentials(message):
    try:
        # الحصول على APP ID و API HASH
        app_id = int(message.text.split()[0])
        api_hash = message.text.split()[1]

        with TelegramClient(StringSession(), app_id, api_hash) as client:
            session_str = client.session.save()
            bot.send_message(message.chat.id, session_str)
            bot.send_message(message.chat.id, "🔼 هذا هو كود التيرمكس الخاص بك لا تعطيه لأي شخص لان معرض للاختراق ❤️ @Scorpions_scorp")
            print("تم إرسال StringSession إلى المحادثة.")

    except Exception as e:
        bot.reply_to(message, f"حدث خطأ: {str(e)}. تأكد من إدخال APP ID و API HASH بشكل صحيح.")

# بدء تشغيل البوت
bot.polling()
