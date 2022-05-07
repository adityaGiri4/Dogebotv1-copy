from telethon import events
from handlers import client
import os
from html_telegraph_poster.upload_images import upload_image

client = client.client


@events.register(events.NewMessage(outgoing=True, pattern=r'\$ sudo upload'))
async def telegraph_upload_handler(event):
    chat = await event.get_chat()
    await client.edit_message(event.message, "ᴘʀᴏᴄᴇssɪɴɢ...")
    replied = await event.get_reply_message()
    try:
        file = await replied.download_media()
        url = upload_image(file)
    except:
        return await client.edit_message(event.message, "ᴅɪs ɪᴢ ɴᴀᴛ ᴀ ᴍᴇᴅɪᴀ ғɪʟᴇ sᴀʀ!")
    await client.edit_message(event.message, f"ᴜᴘʟᴏᴀᴅᴇᴅ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴘʜ!\n{url}", link_preview=False)
    os.remove(file)