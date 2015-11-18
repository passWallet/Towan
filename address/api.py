from tastypie.resources import ModelResource
from tastycrust.resources import ActionResourceMixin, action
from .models import Address


class AddressResource(ActionResourceMixin, ModelResource):
    class Meta:
        queryset = Address.objects.all()
        resource_name = 'address'
        allowed_methods = []

    @action(name="newaddress", allowed=('get',), static=True)
    def new_address(self, request, **kwargs):
        last_address = Address.objects.last()
        if last_address == None:
            pk = 0
        else:
            pk = last_address.pk
        new_address = Address.create(pk)
        context = {'address': new_address}
        new_address.save()
        data = {'public_address': new_address}
        return self.create_response(request, data)
