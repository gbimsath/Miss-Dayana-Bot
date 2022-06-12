import os
import random

from pyrogram.errors.exceptions.bad_request_400 import *
from pyrogram.errors import *
from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import *

#Vars
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY", "")
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME", "")
BOT_TOKEN = os.getenv("BOT_TOKEN")  # from @botfather
API_ID = int(os.getenv("API_ID"))  # from https://my.telegram.org/apps
API_HASH = os.getenv("API_HASH")  # from https://my.telegram.org/apps
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1263393688 2031364837").split())
MONGO_URI = os.getenv("MONGO_URI")
MAIN_CHANNEL = int(os.environ.get("MAIN_CHANNEL", "-1001793793431"))
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001244169300"))
PRIVATE_LOG = int(os.environ.get("PRIVATE_LOG", "-1001745635695"))
force_subchannel = os.getenv("FSUB", "𝑅𝑎𝑤𝑎𝑛𝑎 Partner's")
OWNER_ID = int(os.environ.get("OWNER_ID", "1263393688"))
#Strings 
WELCOME_TEXT = "Hello.. <b>{}</b>\n<code>Type your query here..\nI'll respond to your query as earliest</code> 😉\n\nуσυ ωαииα тσ киσω αвσυт мє😌? яєα∂ вєℓσω\n\nαвσυт @Gishankrishka:-\n •му иαмє:- Gishan Krishka \n •му αgє:- υикиσωи🌝\n •¢σмρυтєя ℓαиgυαgє:- ωєв ∂єνєℓσρмєит(ℓєαяиιиg), ρутнσи мσяє ѕσσи😁\n•¢нє¢к [About ༒❣️☢️╣IrØή❂mคŇ╠☢️❣️༒](https://t.me/Gishankrishka_Info_bot) fσя мσяє\n\nPlz Don't Send Stickers 🥲\nReason :- [This](https://t.me/ultchat/19589)"
USER_DETAILS = "<b>PM FROM:</b>\nName: {} {}\nId: {}\nUname: @{}\nScam: {}\nRestricted: {}\nStatus: {}\nDc Id: {}"
PM_TXT_ATT = "<b>Message from:</b> {}\n<b>Name:</b> {}\n\n{}"
PM_TXT_ATTS = "<b>Message from:</b> {}\n<b>Name:</b> {}"
PM_MED_ATT = "<b>Message from:</b> {} \n<b>Name:</b> {}\n<b>Caption</b>:{}"
USER_DETAILS = "<b>FROM:</b>\nName: {} {}\nId: {}\nUname: @{}\nScam: {}\nRestricted: {}\nStatus: {}\nDc Id: {}"
FORCESUB_TEXT = "**❌ Access Denied ❌**\n\n 𝑅𝑎𝑤𝑎𝑛𝑎 Partner's eke nathuva Mokatada yako Botva Start Kare kkk😒😒\n♻️Join and Try Again.♻️"
HELP_STRING = "Meme Tiye nam dapam Mekata😒😂. Adminlata Msg Daanna One Nam ekat Mekata dapam 😒😂"
START_STRING ="""
Hi {}, Welcome to Sinhala MemeHub Telegram 🇱🇰 Official Bot.
 Bot By [sᴀᵛⁱᵈᵘ ᴅᴇˢʰᵃⁿ](https://t.me/SAVINDU-DESHAN)
"""


#Inline Btn
FORCESUB_BUTTONS = InlineKeyboardMarkup([[
                 InlineKeyboardButton('Join Here - Sinhala MemeHub Telegram', url=f"https://t.me/{force_subchannel}")
                 ],
                 [
                 InlineKeyboardButton('🐞 ʀᴘᴏʀᴛ ʙᴜɢs 🐞', user_id=f"@SAVINDU-DESHAN")
                 ],
                 [
                 InlineKeyboardButton(text="♻️ Reload ♻️",callback_data="ref")
                 ]]
                  )
                  
CLOSE_BUTTON = InlineKeyboardMarkup([[
                 InlineKeyboardButton("𝕮𝖑𝖔𝖒𝖘𝖊", callback_data="cloce")
                 ]]
                 )
                                                    
BACK_BUTTONS = InlineKeyboardMarkup([[
                 InlineKeyboardButton(text="👻 ʙᴀᴍᴄᴋ 👻",callback_data="bak")            
                 ]]
                  ) 

START_BUTTON = InlineKeyboardMarkup([[              
                 InlineKeyboardButton('🍁 Owner 🍁', user_id="@SAVINDU-DESHAN")
                 ],
                 [
                 InlineKeyboardButton(text="🌴 ʜᴇʟᴘ 🌴",callback_data="hlp"),
                 InlineKeyboardButton("🍄 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 🍄", url="https://github.com/SAVINDU-DESHAN/Miss-Dayana-Bot/")
                 ],
                 [
                 InlineKeyboardButton("➕ sʜᴀʀᴇ ➕", switch_inline_query="share"),
                 InlineKeyboardButton("➕ sʜᴀʀᴇ ᴄʜɴʟ ➕", switch_inline_query="cshare")
                 ],
                 [
                 InlineKeyboardButton("𝑅𝑎𝑤𝑎𝑛𝑎 𝐷𝑒𝑣𝑒𝑙𝑜𝑝𝑒𝑟'𝑠 | ∞™", url="https://t.me/Rawana_Developers"),
                 InlineKeyboardButton("රාවණා ᗪι۷ҽʟσᑭɛя'ʂ Chat ", url="https://t.me/Rawana_Developers_Chat")
                 ]]
                  )

ADMIN_BTN = InlineKeyboardMarkup([[
                 InlineKeyboardButton('Sανιη∂υ Dєѕнαη', user_id="SAVINDU_DESHAN")
                 ],[
                 InlineKeyboardButton('#AFK Kushan Imantha', user_id="AFK_Kushan_Imantha")
                 ]]
                  )

OWNER_BTN = InlineKeyboardMarkup([[              
                 InlineKeyboardButton('Sανιη∂υ Dєѕнαη', user_id="SAVINDU_DESHAN")
                 ]]
                  )               

DEV_BTN = InlineKeyboardMarkup([[              
                 InlineKeyboardButton('Sανιη∂υ Dєѕнαη', user_id="SAVINDU_DESHAN")
                 ],
                 [
                 InlineKeyboardButton('Shamal Induwara', user_id="shamalthegreat")
                 ],
                 [
                 InlineKeyboardButton('#AFK Kushan Imantha', user_id="AFK_Kushan_Imantha")
                 ],
                 InlineKeyboardButton('Pulindu Sashmitha', user_id="PulinduSashmitha")
                 ]]
                  )


#Rndm Stkr

OWNER_STICKER = ["CAADAgADtA8AAhUWiEuTU2os6PSW-AI",
                "CAADAgADCwMAAm2wQgN_tBzazKZEJQI",
                "CAADAgADtwEAAladvQr3FVtdLiA1jgI", 
                "CAADBQADSwQAAnxrOFaYSIaXhBE_YAI"              
         ]

STAT_STICKER = ["CAADAQAD7gMAAv5DwUe0nbeQnSoavAI",
                "CAACAgUAAxkBAAEBIxdipaTkP_T2L6lQQPkyyWITgS98dwACfgUAAjOeUVQWJze8PZl5wiQE"              
         ]  

ADMIN_STICKER = ["CAADAgADzhMAAhDzcElTIbO4ZQ8stAI",
                "CAADBQADxwQAAgcbUFea8nhgWIiuGwI",
                "CAADBQADPAUAAtzIoFWtMe3LazkiKQI", 
                "CAADBQADDgQAAkKxWVZAvhW5fKSifwI"              
         ]
         
DEV_STICKER = ["CAADAgADaRsAAsOUWUpHrmf5mZp3EgI",
                "CAADAgADbAIAAladvQoqGV6cxNDenwI",
                "CAADAgADgQEAAiteUwteCmw-bAABeLQC", 
                "CAADBQADZgMAAvIEcFVMnMXcAqRX7gI",
                "CAADAgADFwADlp-MDlZMBDUhRlElAg"                
         ] 

HELP_STICKER = ["CAADAgADYgADWbv8JXMOJcSM3-2OAg",
                "CAADAgADzwEAAhZCawpc3d8UgDDcaQI",
                "CAADAgAD9AIAAvPjvgtVDXi3hHimOQI", 
                "CAADAgADiQEAAiteUwt812TG6sLw9AI"               
         ]


#Menu Btn

start_menu = ReplyKeyboardMarkup(
      [
            ["🤴 OWNER 🤴"],
            ["💻 Bot Devs 💻", "👮‍♂️ MemeHub Admins 👮‍♂️"],
            ["📊 Statistics"]
           
        ],
        resize_keyboard=True  # Make the keyboard smaller
    )

next_1 = ReplyKeyboardMarkup(
      [
            ["📊 Statistics"],
            ["BACK 🔙"]
           
        ],
        resize_keyboard=True  # Make the keyboard smaller
      )

back = ReplyKeyboardMarkup(
      [
            ["🤴 OWNER 🤴"],
            ["💻 Bot Devs 💻", "👮‍♂️ MemeHub Admins 👮‍♂️"],
            ["📊 Statistics"]
           
        ],
        resize_keyboard=True  # Make the keyboard smaller
      )     





print("Config Working....")
