from telethon import events
from handlers import client

client = client.client


@events.register(events.NewMessage(outgoing=True, pattern=r'\$ sudo quote'))
async def quotly_handler(event):
    chat = await event.get_chat()
    replied_message = await event.get_reply_message()
    await client.edit_message(event.message, "ǫᴜᴏᴛɪɴɢ...")
    forward = await replied_message.forward_to("@QuotLyBot")
    async with client.conversation("@QuotLyBot") as convo:
        response = await convo.get_response(forward.id)
        await client.send_read_acknowledge(convo.chat_id)
        await client.send_message(chat, response)
        await event.message.delete()

