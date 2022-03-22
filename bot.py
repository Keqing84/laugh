import os
import json

from Pyrogram import Client as Pyro, filters

class Config:
  id = int(os.environ.get("API_ID"))
  hash = os.environ.get("API_HASH")
  token = os.environ.get("BOT_TOKEN")

TE = Pyro(":memory:", Config.id, Config.hash, Config.token)

@TE.on_message(filters.document)
async def document(message, bot):
   try:
     in_json = message.json()
   except:
     in_json = message
   await message.reply_text(in_json, quote=True)


@TE.on_message(filters.photo)
async def photo(message, bot):
   try:
     in_json = message.json()
   except:
     in_json = message
   await message.reply_text(in_json, quote=True)

@TE.on_message(filters.commamd("start"))
async def start(message, bot):
   replyt = await message.reply_text("Hello User, I Am A Tester Bot For Pyrogram Which My Master @DragonKrak Made For Him")
   try:
     in_json = message.json()
   except:
     in_json = message
   await message.reply_text(in_json, quote=True)
   await replyt.reply_text(replyt, quote=True)
   
@TE.on_message(filters.video)
async def video(message, bot):
   try:
     in_json = message
     in_json.json()
   except:
     in_json = message
   await message.reply_text(in_json)

@TE.on_message(filters.sticker)
async def sticker(message, bot):
   try:
     in_json = message.json()
   except:
     in_json = message
   await message.reply_text(in_json)

@TE.on_message(filters.caption)
async def caption(message, bot):
   try:
     in_json = message.json()
   except:
     in_json = message
   await message.reply_text(in_json)

@TE.on_message(filters.audio)
async def document(message, bot):
   try:
     in_json = message.json()
   except:
     in_json = message
   await message.reply_text(in_json)

@TE.on_message(filters.reply)
async def reply(message, bot):
   try:
     in_json = message.json()
   except:
     in_json = message
   await message.reply_text(in_json)

@TE.on_message(filters.media_group)
async def media_group(message, bot):
   try:
     in_json = message.json()
   except:
     in_json = message
   await message.reply_text(in_json)

@TE.on_message(filters.edited)
async def edited(message, bot):
   try:
     in_json = message.json()
   except:
     in_json = message
   await message.reply_text(in_json)

@TE.on_message(filters.animation)
async def animation(message, bot):
   try:
     in_json = message.json()
   except:
     in_json = message
   await message.reply_text(in_json)



TE.run()
