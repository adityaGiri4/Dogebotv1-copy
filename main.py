# Introducing DogebotXD
# By @StrokesOfSavageness a.k.a. Ash!
import handlers.client
import handlers.alive
import handlers.hello
import handlers.telegraph_upload
import handlers.quotly

client = handlers.client.client

# hello
with client as dogemon:
    dogemon.add_event_handler(handlers.hello.hello_handler)

# alive
with client as dogemon:
    dogemon.add_event_handler(handlers.alive.alive_handler)

# telegraph upload
with client as dogemon:
    dogemon.add_event_handler(handlers.telegraph_upload.telegraph_upload_handler)

# quotly
with client as dogemon:
    dogemon.add_event_handler(handlers.quotly.quotly_handler)

client.start()
client.run_until_disconnected()
