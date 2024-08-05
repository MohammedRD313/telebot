#Developer Bot : @Scorpion_scorp
import os
import requests
import telebot, threading
from telebot import types
from timeit import default_timer as timer
from fake_email import Email
admin = 7275336620 #ايدي المالك

chat_id = "Scorpion_scorp" #يوزر القناة بدون @

dev = "Scorpion_scorp" #يوزر المالك بدون @

token = "7139024104:AAFQwCBzxo0Ru4bNxPc2QP8i6_k8_XO2bNc" # توكن

bot = telebot.TeleBot(token, num_threads=50, skip_pending=True, parse_mode="markdown", disable_web_page_preview=True)
generated_emails = {}
@bot.message_handler(commands=["start"])
def welcome(message):
    x = requests.get(f"https://api.telegram.org/bot{token}/getchatmember?chat_id=@{chat_id}&user_id={message.from_user.id}")
    if any(["member" in x.text, "administrator" in x.text, "creator" in x.text]):
        try:
        	Tho = open("id.txt").read()
        except:
        	oo = open("id.txt", "a")
        	Tho = open("id.txt").read()
        try:
        	ban = open("ban.txt").read()
        except:
        	bb = open("ban.txt", "a")
        	ban = open("ban.txt").read()
        try:
        	ad = open("ad.txt").read()
        except:
        	yy = open("ad.txt", "a")
        	ad = open("ad.txt").read()
        if str(message.from_user.id) == str(admin):
    	    keyboard = types.InlineKeyboardMarkup()
    	    keyboard.row_width = 1
    	    Tho1 = types.InlineKeyboardButton("اذاعة",callback_data="brod")
    	    Tho2 = types.InlineKeyboardButton("أرسل التخزين",callback_data="file")
    	    Tho3 = types.InlineKeyboardButton(f"الأحصائيات",callback_data="info")
    	    Tho4 = types.InlineKeyboardButton(f"حظر مستخدم",callback_data="ban")
    	    Tho5 = types.InlineKeyboardButton(f"مسح المحظورين",callback_data="allun")
    	    Tho6 = types.InlineKeyboardButton(f"الغاء حظر",callback_data="unban")
    	    Tho7 = types.InlineKeyboardButton(f"رفع أدمن",callback_data="adad")
    	    Tho8 = types.InlineKeyboardButton(f"تنزيل أدمن",callback_data="unad")
    	    Tho9 = types.InlineKeyboardButton(f"مسح جميع الادمنية",callback_data="rmad")
    	    keyboard.row(Tho3, Tho2)
    	    keyboard.row(Tho1)
    	    keyboard.row(Tho6, Tho4)
    	    keyboard.row(Tho5)
    	    keyboard.row(Tho8, Tho7)
    	    keyboard.row(Tho9)
    	    bot.reply_to(message, f"*أهلا بك عزيزي المالك*", reply_markup=keyboard)
    	    btn = types.InlineKeyboardMarkup()
    	    btn.row_width = 1
    	    ah = types.InlineKeyboardButton("قـنـاتـنـا", url=f"t.me/{dev}")
    	    gen_email = types.InlineKeyboardButton("إنشاء حساب بريد", callback_data='generate_email')
    	    get_ms = types.InlineKeyboardButton("جلب الرسائل الواردة", callback_data='fetch_messages')
    	    btn.add(ah,gen_email,get_ms)
    	    bot.reply_to(message, "أهلا بك عزيزي المستخدم", reply_markup=btn)
    	    
        elif str(message.from_user.id) in ban:
        	bot.reply_to(message, "*تم حظرك من البوت\nللأستفسار عن السبب راسل المطور*")
        elif str(message.from_user.id) in ad:
    	    keyboard = types.InlineKeyboardMarkup()
    	    keyboard.row_width = 1
    	    Tho1 = types.InlineKeyboardButton("اذاعة",callback_data="brod")
    	    Tho3 = types.InlineKeyboardButton(f"الأحصائيات",callback_data="info")
    	    Tho4 = types.InlineKeyboardButton(f"حظر مستخدم",callback_data="ban")
    	    Tho6 = types.InlineKeyboardButton(f"الغاء حظر",callback_data="unban")
    	    keyboard.row(Tho1, Tho3)
    	    keyboard.row(Tho4, Tho6)
    	    bot.reply_to(message, f"*أهلا بك عزيزي الادمن*", reply_markup=keyboard)
    	    btn = types.InlineKeyboardMarkup()
    	    btn.row_width = 1
    	    ah = types.InlineKeyboardButton("المطور", url=f"t.me/{dev}")
    	    gen_email = types.InlineKeyboardButton("إنشاء حساب بريد", callback_data='generate_email')
    	    get_ms = types.InlineKeyboardButton("جلب الرسائل الواردة", callback_data='fetch_messages')
    	    btn.add(gen_email,get_ms)
    	    bot.reply_to(message, "أهلا بك عزيزي المستخدم", reply_markup=btn)
    	    
        elif str(message.from_user.id) in Tho:
            btn = types.InlineKeyboardMarkup()
            btn.row_width = 1
            ah = types.InlineKeyboardButton(text="المطور", url=f"t.me/{dev}")
            gen_email = types.InlineKeyboardButton("إنشاء حساب بريد", callback_data='generate_email')
            get_ms = types.InlineKeyboardButton("جلب الرسائل الواردة", callback_data='fetch_messages')
            btn.add(ah,gen_email,get_ms)
            bot.reply_to(message, "أهلا بك عزيزي المستخدم", reply_markup=btn)
        else:
    	    with open("id.txt", "a") as Ah:
    	    	Ah.write(f"{message.from_user.id}\n")
    	    bot.reply_to(message, "*تم تفعيل البوت\nأرسل /start*")
    	    bot.send_message(admin, f"*مستخدم جديد:\nإسمه:* {message.from_user.first_name} .\n*يوزرة:* @{message.from_user.username} .\n*أيديه:* `{message.from_user.id}` .\n[المبرمج](t.me/{dev})")
    else:
    	bot.reply_to(message, f"*لازم تشترك بقناة البوت حتى تكدر تستخدمة\n\n- @{chat_id}*")

@bot.callback_query_handler(func=lambda call: True)
def calldata(call):
    if call.data == "brod":
    	bot.send_message(call.message.chat.id, "*أرسل رسالة الاذاعة\nتگدر تستعمل ماركداون همين*")
    	bot.register_next_step_handler(call.message, brod)
    	
    if call.data == "file":
    	bot.send_document(admin, open('id.txt','rb'))
    	try:
    		bot.send_document(admin, open('ban.txt','rb'))
    	except:
    		bot.send_message(admin, "*لايوجد محظورين لأرسال ملفهم*")

    if call.data == "info":
    	Th = open("id.txt", "r")
    	Of = open("ban.txt", "r")
    	adr = open("ad.txt", "r")
    	qa = len(Th.readlines())
    	ar = len(Of.readlines())
    	ad = len(adr.readlines())
    	bot.send_message(call.message.chat.id, f"*أهلا بك عزيزي الادمن في قسم الاحصائيات\nعدد مستخدمين البوت: {qa}.\nعدد المحظورين: {ar}.\nعدد الأدمنية: {ad}.*")
    	Th.close()
    	Of.close()
    	adr.close()
    	
    if call.data == "ban":
    	bot.send_message(call.message.chat.id, "*أرسل الايدي الذي تريد حظره*")
    	bot.register_next_step_handler(call.message, ban)
    	
    if call.data == "allun":
    	try:
    		bot.send_document(admin, open('ban.txt','rb'))
    		os.remove("ban.txt")
    		bot.send_message(admin, "*تم مسح جميع المحظورين و أرسال لك نسخة احتياطية*")
    	except:
    		bot.send_message(call.message.chat.id, "*لا يوجد محظورين*")

    if call.data == "rmad":
    	try:
    		os.remove("ad.txt")
    		bot.send_message(admin, "تمت حبي")
    	except:
    		bot.send_message(call.message.chat.id, "*لا يوجد ادمنيه*")
 
    if call.data == "unban":
    	bot.send_message(call.message.chat.id, "*أرسل الايدي الذي تريد الغاء حظره*")
    	bot.register_next_step_handler(call.message, unban)

    if call.data == "adad":
    	bot.send_message(call.message.chat.id, "*أرسل أيدي المستخدم*")
    	bot.register_next_step_handler(call.message, adad)
    	
    if call.data == "unad":
    	bot.send_message(call.message.chat.id, "*أرسل أيدي المستخدم*")
    	bot.register_next_step_handler(call.message, unad)    	
    if call.data == "generate_email":
        generate_email(call.message)
    elif call.data == "fetch_messages":
        fetch_messages(call.message)
def unad(message):
	id = message.text
	unad = open("ad.txt").read()
	if id not in unad:
		bot.reply_to(message, "مو أدمن اصلا هذا")
	else:
		name = "ad.txt"
		with open(name, 'r', encoding='utf-8') as file:
			lines = file.readlines()
		lines = [line for line in lines if id not in line]
		with open(name, 'w', encoding='utf-8') as file:
			file.writelines(lines)
		bot.send_message(id, "*تم تنزيلك من الادمنية*")
		bot.reply_to(message, "*تمت حب*")
#Developer Bot : @Scorpion_scorp 
def adad(message):
    id = message.text
    ad = open("ad.txt").read()
    if id in ad:
    	bot.reply_to(message, "*هذا المستخدم اصلا أدمن*")
    else:
        with open("ad.txt", "a") as Ah:
        	Ah.write(f"{id}\n")
        bot.send_message(id, "*تم رفعك ادمن بالبوت*")
        bot.reply_to(message, "*تمت حبي*")	
#Developer Bot : @Scorpion_scorp
def unban(message):
	id = message.text
	unbann = open("ban.txt").read()
	if id not in unbann:
		bot.reply_to(message, "مو محظور اصلا حبي")
	else:
		name = "ban.txt"
		with open(name, 'r', encoding='utf-8') as file:
			lines = file.readlines()
		lines = [line for line in lines if id not in line]
		with open(name, 'w', encoding='utf-8') as file:
			file.writelines(lines)
		bot.send_message(id, "*تم الغاء حظرك الان!*")
		bot.reply_to(message, "*تمت حب*")
#Developer Bot : @Scorpion_scorp
def ban(message):
    id = message.text
    bann = open("ban.txt").read()
    if id in bann:
    	bot.reply_to(message, "*هذا المستخدم اصلا محظور حبي*")
    else:
        with open("ban.txt", "a") as Ah:
        	Ah.write(f"{id}\n")
        bot.send_message(id, "*تم حظرك من البوت\nللأستفسار راسل المطور*")
        bot.reply_to(message, "*تمت حبي*")
#Developer Bot : @Scorpion_scorp
def brod(message):
    msg = message.text
    bot.send_message(admin, msg)    
    ids = open("id.txt", "r").readlines()
    i = 0
    F = 0
    T = 0
    start = timer()
    for Id in ids:
        i = i + 1
        try:
            bot.send_message(Id, msg)
            T = T + 1
        except:
            F = F + 1
    end = timer()
    ttt = end - start
    bot.reply_to(message, f'''*عدد المستخدمين: {len(ids)}
تمت الاذاعة لـ: {T}/{len(ids)}
فشلت لـ: {F}/{len(ids)}
أجمالي وقت الاذاعة : {int(ttt)}*''')
def generate_email(message):
    email = Email().Mail()
    generated_emails[message.chat.id] = email
    bot.send_message(message.chat.id, f"تم إنشاء بريد وهمي جديد:\n`{email['mail']}`", parse_mode='MarkdownV2')
def fetch_messages(message):
    if message.chat.id in generated_emails:
        email = generated_emails[message.chat.id]
        messages = Email(email["session"]).inbox()
        if messages:
            bot.send_message(message.chat.id, f"الرسائل الواردة:\ntopic: {messages['topic']}\nname: {messages['name']}\nfrom: {messages['from']}\nto: {messages['to']}\nmessage: {messages['message']}")
        else:
            bot.send_message(message.chat.id, "لا توجد رسائل واردة حالياً")
    else:
        bot.send_message(message.chat.id, "يرجى إنشاء حساب بريد إلكتروني أولاً")
print("-- Bot Started...")
#Developer Bot : @Scorpion_scorp
bot.infinity_polling()
