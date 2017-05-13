from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastycrust.resources import ActionResourceMixin, action
from tastypie.constants import ALL
from .models import Address
from random import randint
import json
import blocktrailAPI

from channels import Group

class AddressResource(ActionResourceMixin, ModelResource):
    class Meta:
        queryset = Address.objects.all()
        resource_name = 'address'
        allowed_methods = []

    @action(name="new_address", allowed=('get',), static=True)
    def new_address(self, request, **kwargs):
        queryset = Address.objects.all().order_by('-id')[0:20]
        used_address_list = [item for item in queryset if item.used]
        if (len(used_address_list)>0 or len(queryset)<20):
            last_address = Address.objects.last()
            if last_address == None:
                pk = 0
            else:
                pk = last_address.pk
            new_address = Address.create(pk)
            context = {'address': new_address}
            new_address.save()
        else :
            rand = randint(0,19)
            new_address = [item for item in queryset if not(item.used)][rand]
        data = {'public_address': new_address}
        return self.create_response(request, data)

    @action(name="payment_received", allowed=('post',), static=True)
    def payment_received(self, request, **kwargs):
        response = json.loads(request.body)
        address = response['addresses'].keys()[0]
        queryset = Address.objects.get(address=address)
        queryset.used = True
        queryset.save()
        blocktrailAPI.unsubscribe_address_event(queryset.address)
        Group(queryset.address).send({'text': 'payment_received'})
        return self.create_response(request, request.body)


    #@action(name="helloworld", allowed=('get','post'), static=True)
    #def new_address(self, request, **kwargs):
    #    print request.body
    #    return self.create_response(request, request.body)

# # # # # # # # # # # # # # # # # # #
# Admin ressources for towan-client #
# # # # # # # # # # # # # # # # # # #

class AdminAddressResource(ActionResourceMixin, ModelResource):
    class Meta:
        queryset = Address.objects.all().order_by('-id')
        resource_name = 'address'
        list_allowed_methods = ['get']
        authentication = ApiKeyAuthentication()
        ordering = ALL
