from __future__ import print_function
from django.db import models
from bitmerchant.wallet import Wallet
from bitmerchant.network import BitcoinTestNet
import blocktrailAPI
# from address.models import Address


ADDRESS_MAX_LENGTH = 34
PUBLIC_KEYCHAIN_TESTNET = "tpubDCBUQADzsuBscd823dnNWeo2kefBohWR9GUWeB3ztfLuCPgYer3BBxNJfzZiSAXp2UegvGWoRZUbTKtqx9Ve5qt8J72kRuwSuF9U8cgpszp"

class Address(models.Model):
    address = models.CharField(max_length=ADDRESS_MAX_LENGTH, blank=True, help_text="Bitcoin Address", unique=True, editable=False)
    used = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.address

    @classmethod
    def create(self, id):
        child_pubkey = Wallet.deserialize(PUBLIC_KEYCHAIN_TESTNET, BitcoinTestNet).get_child(0).get_child(id)
        address = child_pubkey.to_address()
        blocktrailAPI.subscribe_address_event(address)
        return self(address=address)

    class Meta:
        verbose_name_plural = "Addresses"
