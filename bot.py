import Ai
from pyrogram import Client,filters

API_ID = 14170449
API_HASH = "03488b3c030fe095667e7ca22fe34954"
TOKEN = "7202104518:AAFeZK4Dz9GclJKV0kXOG1Vr9jY3BhPazzU:"
app = Client("ChatGpt", api_id=API_ID,api_hash=API_HASH,bot_token=TOKEN) 


@app.on_message(filters.command("start"))
async def StartMsg(_,msg):
 await msg.reply("Hello: I am ChatGpt")
 
@app.on_message(filters.command("بوت",""))
async def YesSir(_,msg):
 await msg.reply("مرحبا بك عزيزي : اسمي هو ميجا")
 

@app.on_message(filters.private & ~filters.reply)
async def echo(bot, msg):
    a = msg.text
    s = Ai(query = a)
    await bot.send_message(chat_id=msg.chat.id, text=s.chat()) 
    

@app.on_message(filters.text)
async def reply(bot, msg):
  try:
    if  msg.reply_to_message.from_user.is_bot:
    	a = msg.text
    	s = Ai(query = a)
    	await msg.reply_text(text=s.chat(),quote=True)
  except:pass
    
@app.on_message(filters.regex(r"^ميجا (.+)"),group=-1)
async def reply_with_text(bot, msg):
    a = msg.text.split(None,1)[1]
    s = Ai(query = a)
    await msg.reply_text(text=s.chat(),quote=True)
    
    
 
print("Run..")   
app.run()
