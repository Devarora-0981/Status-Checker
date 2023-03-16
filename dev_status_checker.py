#Copyright ©️ 2022 Dev Arora. All Rights Reserved.
import os
import re
import pytz
import asyncio
import datetime

from pyrogram import Client, filters
from pyrogram.errors import FloodWait


app = Client(
    name = "devbotz",
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    session_string = os.environ["SESSION_STRING"]
)

TIME_ZONE = os.environ["TIME_ZONE"]
BOT_LIST = [i.strip() for i in os.environ.get("BOT_LIST").split(' ')]
CHANNEL_ID = int(os.environ["CHANNEL_ID"]) #CHANNEL_ID is for group/channel where checker will update the status.
MESSAGE_ID = int(os.environ["MESSAGE_ID"])
BOT_ADMIN_IDS = [int(i.strip()) for i in os.environ.get("BOT_ADMIN_IDS").split(' ')]
GRP_ID = os.environ.get("GRP_ID") #GRP_ID is for logs group where checker will send warnings of offline bots.

async def main_devchecker():
    async with app:
            while True:
                print("Checking...")
                xxx_teletips = f"<u>**🏷 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {(await app.get_chat(CHANNEL_ID)).title} ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴄʜᴀɴɴᴇʟ**</u>\n\n 📈 | <u>**ʀᴇᴀʟ ᴛɪᴍᴇ ʙᴏᴛ's sᴛᴀᴛᴜs 🍂**</u>"
                for bot in BOT_LIST:
                    await asyncio.sleep(7)
                    try:
                        bot_info = await app.get_users(bot)
                    except Exception:
                        bot_info = bot

                    try:
                        yyy_teletips = await app.send_message(bot, "/start")
                        aaa = yyy_teletips.id
                        await asyncio.sleep(15)
                        zzz_teletips = app.get_chat_history(bot, limit = 1)
                        async for ccc in zzz_teletips:
                            bbb = ccc.id
                        if aaa == bbb:
                            xxx_teletips += f"\n\n╭⎋ **[{bot_info.first_name}](tg://user?id={bot_info.id})**\n╰⊚ **sᴛᴀᴛᴜs: ᴏғғʟɪɴᴇ ❄**"
                            for bot_admin_id in BOT_ADMIN_IDS:
                                try:
                                    await app.send_message(int(GRP_ID), f"**ʙsᴅᴋ ᴋʏᴀ ᴋᴀʀ ʀᴀʜᴀ ʜᴀɪ 😡\n[{bot_info.first_name}](tg://user?id={bot_info.id}) ᴏғғ ʜᴀɪ. ᴀᴄᴄʜᴀ ʜᴜᴀ ᴅᴇᴋʜ ʟɪʏᴀ ᴍᴀɪɴᴇ.**")
                                except Exception:...
                            await app.read_chat_history(bot)
                        else:
                            xxx_teletips += f"\n\n╭⎋ **[{bot_info.first_name}](tg://user?id={bot_info.id})**\n╰⊚ **sᴛᴀᴛᴜs: ᴏɴʟɪɴᴇ ✨**"
                            await app.read_chat_history(bot)
                    except FloodWait as e:
                        ttm = re.findall("\d{0,5}", str(e))
                        await asyncio.sleep(int(ttm))
                time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
                last_update = time.strftime(f"%d %b %Y at %I:%M %p")
                xxx_teletips += f"\n\n✔️ <u>ʟᴀsᴛ ᴄʜᴇᴄᴋᴇᴅ ᴏɴ:</u>\n**ᴅᴀᴛᴇ & ᴛɪᴍᴇ: {last_update}**\n**ᴛɪᴍᴇ ᴢᴏɴᴇ: ({TIME_ZONE})**\n\n<i><u>♻️ ʀᴇғʀᴇsʜᴇs ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴡɪᴛʜɪɴ 10 ᴍɪɴᴜᴛᴇs.</u></i>\n\n<b>**๏ ᴘᴏᴡᴇʀᴇᴅ ʙʏ @{(await app.get_chat(CHANNEL_ID)).username} ๏**</b>"
                await app.edit_message_text(int(CHANNEL_ID), MESSAGE_ID, xxx_teletips)
                print(f"Last checked on: {last_update}")                
                await asyncio.sleep(600)
                        
app.run(main_devchecker())

#Copyright ©️ 2022 Dev Arora. All Rights Reserved.
