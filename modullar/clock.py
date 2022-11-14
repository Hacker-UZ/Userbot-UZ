from telethon import TelegramClient, events
from telethon.tl.functions.account import UpdateProfileRequest
import asyncio
import datetime
import modullar.client
client = modullar.client.client


@events.register(events.NewMessage(outgoing=True))
async def clock(event):
    if ".clock" in event.raw_text:
        while True:
            client = event.client
            me = await client.get_me()
            username = me.username
            time = datetime.datetime.today().strftime("{} | %H:%M".format(username))
            async with client:
                await client(UpdateProfileRequest(first_name=time))
                await asyncio.sleep(60)
