from channels.sessions import channel_session
from tastypie.models import ApiKey
from django.contrib.auth.models import User
from channels import Group
from urllib import parse

# TODO: Seperate in different modules

###################################
# Websocket connection on frontend
###################################

# Connected to websocket.connect
@channel_session
def basic_connect(message):
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
def basic_disconnect(message):
    if (message.channel_session['address']) :
        Group(message.channel_session['address']).discard(message.reply_channel)

###################################
# Websocket connection on client
###################################

# Connected to websocket.connect
def client_connect(message):
    data = dict(message['headers'])['authorization']
    data = data.split()
    username, api_key = data[1].split(':', 1)
    if not username or not api_key:
        message.reply_channel.send({"accept": False})
    else:
        try:
            user = User.objects.select_related('api_key').get(username=username)
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            message.reply_channel.send({"accept": False})
            return

        try :
            if user.api_key.key != api_key:
                message.reply_channel.send({"accept": False})
        except ApiKey.DoesNotExist:
            message.reply_channel.send({"accept": False})

        message.reply_channel.send({"accept": True})
        Group('client').add(message.reply_channel)

# Connected to websocket.disconnect
def client_disconnect(message):
    Group('client').discard(message.reply_channel)
