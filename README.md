# TOWAN Project (The One Without A Name) #
=========================================

## Presentation ##

Little raspberry pi project that allow a user to transform a complicate bitcoin address in a readable human URL.

## Explication ##

TOWAN offer a endpoint that send a new bitcoin address everytime it is called (HD). It also offer a little interface for the owner.

## Notes ##

### Generate Public Testnet Master Key ###

see bitmerchant lib.

```
## DO THIS ON AN OFFLINE MACHINE, NOT YOUR WEBSERVER
from bitmerchant.wallet import Wallet
from bitmerchant.network import BitcoinTestNet

# Create a wallet, and a primary child wallet for your app
my_wallet = Wallet.new_random_wallet(None, BitcoinTestNet )
print(my_wallet.serialize_b58(private=True))  # Private Testnet Master Key (To be keep somewhere safe)
project_0_wallet = my_wallet.get_child(0, is_prime=True)
project_0_public = project_0_wallet.public_copy()
print(project_0_public.serialize_b58(private=False))  # Public Testnet Master Key
```

### Derives Public Testnet Key ###

```
## THINGS BELOW ARE PUBLIC FOR YOUR WEBSERVER

# In your app's settings file, declare your public wallet:
WALLET_PUBKEY = "<public output from above>"

# Create a payment address for a user as needed:
from bitmerchant.wallet import Wallet
from bitmerchant.network import BitcoinTestNet
from myapp.settings import WALLET_PUBKEY

def get_payment_address_for_user(user):
    user_id = user.id
    assert isinstance(user_id, (int, long))
    wallet = Wallet.deserialize(WALLET_PUBKEY, BitcoinTestNet)
    wallet_for_user = wallet.create_new_address_for_user(user.id)
    return wallet_for_user.to_address()
```
