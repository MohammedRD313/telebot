
__author__ = "@DevBoda - @Y_U_A_F"
__channel__ = "@YO0OD"

from pyrogram import Client,filters,idle
from pyrogram.types import (
InlineKeyboardMarkup as Key,
InlineKeyboardButton as Button,
Message,CallbackQuery
)
import requests
from redis import Redis

client = Client(
"quran-YO0OD",
api_id=" 21428087",
api_hash="9f8310fcd0b022c7c09ec658a6bba1dd",
bot_token="7231254366:AAHkHtHowT9Sd5iBVJNTqNMdN51uvLPrGsk"
)

client.start()
r = Redis(decode_responses=True)

def page(num):
	url = f"https://quran.ksu.edu.sa/png_big/{num}.png"
	return url

def buttons(page):
	if page == 1:
		return Key([[
		Button(f"Current page ❬ {page} ❭",
		callback_data='cp')],[
		Button(f"Next Page ❬ {page+1} ❭",
		callback_data=f"n {int(page)+1}")],[
		Button('رجوع',
		callback_data='pool')]])
	elif page == 604:
		return Key([[
		Button(f"Current page ❬ {page} ❭",
		callback_data='cp')],[
		Button(f"Last Page ❬ {page-1} ❭",
		callback_data=f"l {int(page)-1}")],[
		Button('رجوع',
		callback_data='pool')]])
	else:
		return Key([[
		Button(f"Current page ❬ {page} ❭",
		callback_data='cp')],[
		Button(f"Last Page ❬ {page-1} ❭",
		callback_data=f"l {page-1}"),
		Button(f"Next Page ❬ {page+1} ❭",
		callback_data=f"n {page+1}")],[
		Button('رجوع',
		callback_data='pool')]])
		

startB = Key([[
Button("بدء القراءة",
callback_data='st'),
Button("بحث عن صفحه",
callback_data='sr')],[
Button("DevBoda",
user_id=6118310038)]])

@client.on_message(filters.command("start")&filters.private)
async def start(c:Client,m:Message):
	return await m.reply_text(
	"**مرحبا {} في بوت المصحف 💗\nاضغط الزر لبدء القراءة 💗\nيمكنك الوصول لصفحه معينه عن طريق الزر 💗**".format(m.from_user.mention),
	reply_markup=startB)
	
@client.on_callback_query(filters.regex("^n (\\d+)|^l (\\d+)"))
async def next(c:Client,query:CallbackQuery):
	await query.message.delete()
	await query.message.reply_photo(
	page(query.data.split(' ')[1]),
	caption='❤',
	reply_markup=buttons(int(query.data.split(' ')[1])))

@client.on_callback_query()
async def calls(c:Client,query:CallbackQuery):
	if query.data == "st":
		await query.message.delete()
		await query.message.reply_photo(
		page(1),
		reply_markup=buttons(1),
		caption="❤")
		return
	if query.data == "sr":
		r.set(f'w {query.from_user.id}',0)
		await query.message.edit(
		"**ارسل رقم الصفحه الآن من 1 الي 604.!**",
		reply_markup=Key([[
		Button('رجوع',
		callback_data='back')]]))
		return
	if query.data == "back":
		r.delete(f"w {query.from_user.id}")
		return await query.message.edit(
	"**مرحبا {} في بوت المصحف 💗\nاضغط الزر لبدء القراءة 💗\nيمكنك الوصول لصفحه معينه عن طريق الزر 💗**".format(query.from_user.mention),
		reply_markup=startB)
	if query.data == "^bkkk$":
		return await query.message.edit(
		"**مرحبا {} في بوت المصحف 💗\nاضغط الزر لبدء القراءة 💗\nيمكنك الوصول لصفحه معينه عن طريق الزر 💗**".format(query.from_user.mention),
		reply_markup=startB)
	if query.data == "pool":
		await query.message.delete()
		await query.message.reply_text(
		"**مرحبا {} في بوت المصحف 💗\nاضغط الزر لبدء القراءة 💗\nيمكنك الوصول لصفحه معينه عن طريق الزر 💗**".format(query.from_user.mention),
		reply_markup=startB)
	
@client.on_message(filters.text&filters.private)
async def src(c:Client,m:Message):
	if not r.get(f"w {m.from_user.id}"):pass
	else:
		r.delete(f"w {m.from_user.id}")
		try:
			return await m.reply_photo(
			page(int(m.text)),
			caption="❤",
			reply_markup=buttons(int(m.text)))
		except Exception as e:
			print(e)
			return await m.reply(
			"**يجب ارسال رقم بين 1 و 604.!**",
			reply_markup=Key([[
			Button('رجوع',callback_data='back')]]))

idle()
