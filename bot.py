import telebot
from telebot import types

API_TOKEN = 'YOUR_API_TOKEN'
CHANNEL_ID = '@your_channel_username'  # استبدل باسم قناتك
DEV_USER_ID = 123456789  # Замените на ваш user ID
bot = telebot.TeleBot(API_TOKEN)

# قائمة المستخدمين المحظورين
banned_users = set()
# قائمة المستخدمين المشتركين
subscribed_users = set()

# وظيفة للتحقق من الاشتراك
def check_subscription(user_id):
    try:
        chat_member = bot.get_chat_member(CHANNEL_ID, user_id)
        return chat_member.status in ['member', 'administrator', 'creator']
    except Exception as e:
        return False  # إذا حدث خطأ، المستخدم غير مشترك

@bot.message_handler(commands=['abmn'])
def start(message):
    user_id = message.from_user.id

    # التحقق مما إذا كان المستخدم محظورًا
    if user_id in banned_users:
        bot.send_message(message.chat.id, "أنت محظور.")
        return

    # التحقق من الاشتراك
    if not check_subscription(user_id):
        bot.send_message(message.chat.id, "الاشتراك إجباري، يرجى الاشتراك في القناة لتتمكن من استخدام البوت.")
        return

    # إشعار بالدخول
    bot.send_message(message.chat.id, f"مرحبًا، {message.from_user.first_name}!")

@bot.message_handler(commands=['ban'])
def ban_user(message):
    if message.from_user.id != DEV_USER_ID:
        bot.send_message(message.chat.id, "ليس لديك الإذن لاستخدام هذا الأمر.")
        return

    try:
        user_id = int(message.text.split()[1])
        banned_users.add(user_id)
        bot.send_message(message.chat.id, f"تم حظر المستخدم {user_id}.")
    except (IndexError, ValueError):
        bot.send_message(message.chat.id, "يرجى تحديد معرف صحيح للمستخدم لحظره.")

@bot.message_handler(commands=['subscribe'])
def subscribe(message):
    user_id = message.from_user.id
    subscribed_users.add(user_id)
    bot.send_message(message.chat.id, "لقد اشتركت!")

# بدء تشغيل البوت
if __name__ == '__main__':
    bot.polling(none_stop=True)
