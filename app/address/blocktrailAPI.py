from django.conf import settings
from getenv import env

import blocktrail


#Blocktrail API config
NETWORK = env('NETWORK','BTC')
TESTNET = env('TESTNET', True)

#Blocktrail webhook
IDENTIFIER = env('IDENTIFIER', 'localhost')
CONFIRMATIONS = 0

client = blocktrail.APIClient(api_key=settings.MY_APIKEY, api_secret=settings.MY_APISECRET, network=NETWORK, testnet=TESTNET)

def subscribe_address_event(address):
    """ Suscribe to blocktrail transaction event webhook on address """
    try:
        client.subscribe_address_transactions(identifier=IDENTIFIER, address=address, confirmations=CONFIRMATIONS)
    except Exception as e:
        print '%s (%s)' % (e.message, type(e))

def unsubscribe_address_event(address):
    """ Unsuscribe to blocktrail transaction event webhook on address """
    try:
        client.unsubscribe_address_transactions(identifier=IDENTIFIER, address=address)
    except Exception as e:
        print '%s (%s)' % (e.message, type(e))
