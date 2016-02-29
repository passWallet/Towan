from django.conf import settings

import blocktrail


#Blocktrail API config
NETWORK = "BTC"
TESTNET = True

#Blocktrail webhook
IDENTIFIER = "towan"
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
