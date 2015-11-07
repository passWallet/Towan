from django.db import models
from bitmerchant.wallet import Wallet
from bitmerchant.network import BitcoinTestNet
# from address.models import Address

ADDRESS_MAX_LENGTH = 34
PUBLIC_KEYCHAIN_TESTNET = "tpubD9QYaeMbwnAhx6D8CeUqFpTZCu5zYBv8m8AjE3vdUs2kDFjSr2SqurVwCiLAiimBFYGasUSpFHNeykF2vi5AbWfPGyFQnyEfhd5ngKESkqQ"
# tprv8ZgxMBicQKsPemV9DQWnbY6faGowm5g1UQURonLnPM12anyYJ9Jt9mqWcHToyzV9MTx82bayQaQx1LtsBM7xBksSo6HVPRtKPYXMUxVjCo9

class Address(models.Model):
    address = models.CharField(max_length=ADDRESS_MAX_LENGTH, blank=True, help_text="Bitcoin Address", unique=True, editable=False)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.address

    @classmethod
    def create(self, id):
        child_pubkey = Wallet.deserialize(PUBLIC_KEYCHAIN_TESTNET, BitcoinTestNet).get_child(id)
        address = child_pubkey.to_address()
        return self(address=address)

    class Meta:
        verbose_name_plural = "Addresses"
