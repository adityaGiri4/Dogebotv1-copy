from telethon import events
from handlers import client


client = client.client


@events.register(events.NewMessage(outgoing=True, pattern=r'\$ sudo alive'))
async def alive_handler(event):
    chat = await event.get_chat()
    me = await client.get_me()
    await client.delete_messages(chat, event.message)
    await client.send_file(chat, file="photo_2022-05-02_14-19-19.jpg", caption=
    "ᴅᴏɢᴇʙᴏᴛ ɪs ɴᴏᴛ sʟᴇᴇᴍᴘɪɴɢ sᴀʀ; ʜᴇ ɪᴢ ᴀʟɪᴠᴇ!\n"
    "バカ!ふざけん \n\n"
    "$ ᴄʀᴇᴀᴛᴏʀ - @CalmLegend\n"
    "$ ᴍᴀᴅᴇ ᴜsɪɴɢ ᴘʏᴛʜᴏɴ - 𝟹.𝟷𝟶.𝟺\n"
    "$ ᴛᴇʟᴇᴛʜᴏɴ - 𝟷.𝟸𝟻.𝟷")
