from channels.sessions import channel_session
from channels import Group

# Connected to websocket.connect
@channel_session
def ws_connect(message, address):
    message.channel_session['address'] = address
    # Add connection to address group (should have only one connection)
    Group(address).add(message.reply_channel)

# Connected to websocket.disconnect
@channel_session
def ws_disconnect(message):
    if (message.channel_session['address']) :
        Group(message.channel_session['address']).discard(message.reply_channel)
