# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL | LISA-KOREA/YouTube-Video-Download-Bot

# [⚠️ Do not change this repo link ⚠️] :- https://github.com/LISA-KOREA/YouTube-Video-Download-Bot

from pyrogram import Client, filters
import datetime
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply
from Youtube.config import Config
from Youtube.script import Translation
from Youtube.forcesub import handle_force_subscribe


#########################

# Calculate current time greeting
currentTime = datetime.datetime.now()
if currentTime.hour < 12:
    wish = "Good morning 🌞"
elif 12 <= currentTime.hour < 18:
    wish = "Good afternoon 🌤️"
else:
    wish = "Good evening 🌝"




########################🎊 Lisa | NT BOTS 🎊######################################################
@Client.on_callback_query(filters.regex("cancel"))
async def cancel(client, callback_query):
    await callback_query.message.delete()

# About command handler
@Client.on_message(filters.private & filters.command("about"))
async def about(client, message):
    if Config.CHANNEL:
      fsub = await handle_force_subscribe(client, message)
      if fsub == 400:
        return
    await message.reply_text(
        text=Translation.ABOUT_TXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton('⛔️ Close', callback_data='cancel')]
        ]
    ))


# Start command handler
@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    if Config.CHANNEL:
      fsub = await handle_force_subscribe(client, message)
      if fsub == 400:
        return
    #user = message.from_user
    await message.reply_text(
        text=Translation.START_TEXT.format(message.from_user.first_name, wish),
        reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('🇮🇳 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ 🇮🇳', url='https://t.me/synaxnetwork'),
            ],
            [
                InlineKeyboardButton('🌷 ᴏᴡɴᴇʀ 🌷', url='https://t.me/sanatanisynax'),
                InlineKeyboardButton('🇮🇳 sᴜᴘᴘᴏʀᴛ 🇮🇳', url='https://t.me/synaxchatgroup'),
            ],
            [
                InlineKeyboardButton('🗑️ ᴄʟᴏsᴇ 🗑️', callback_data='cancel')
            ]
        ]
    ))

# Help command handler
@Client.on_message(filters.command("help"))
def help(client, message):
    help_text = """
    ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ʏᴛ ᴠɪᴅᴇᴏ 
ᴜᴘʟᴏᴀᴅᴇʀ ʙᴏᴛ 🇮🇳💗

✰ ᴛᴏ ᴜᴘʟᴏᴀᴅ ᴀ ʏᴛ ᴠɪᴅᴇᴏ , 
     sɪᴍᴘʟʏ sᴇɴᴅ ᴍᴇ ᴛʜᴇ ʏᴛ ʟɪɴᴋ.

🇮🇳💗 ᴄʜᴀɴɴᴇʟ : @synaxbots
    """
    message.reply_text(help_text)

########################🎊 Lisa | NT BOTS 🎊######################################################
