from channels.sessions import channel_session
from channels import Group
from urllib import parse

# Connected to websocket.connect
@channel_session
def ws_connect(message):
    query = parse.parse_qs(message['query_string'])
    if 'address' not in query:
        return
    address = query['address'][0]
    message.channel_session['address'] = address
    message.reply_channel.send({"accept": True})
    # Add connection to address group (should have only one connection)
    Group(address).add(message.reply_channel)

# Connected to websocket.disconnect
@channel_session
def ws_disconnect(message):
    if (message.channel_session['address']) :
        Group(message.channel_session['address']).discard(message.reply_channel)
