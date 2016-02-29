from django.shortcuts import render
from django.http import HttpResponse
from .models import Address
from random import randint


def index(request):
    queryset = Address.objects.all().order_by('-id')[0:20]
    used_address_list = [item for item in queryset if item.used]
    if (len(used_address_list)>0 or len(queryset)<20):
        last_address = Address.objects.last()
        if last_address == None:
            pk = 0
        else:
            pk = last_address.pk
        new_address = Address.create(pk)
        new_address.save()
    else :
        rand = randint(0,19)
        new_address = [item for item in queryset if not(item.used)][rand]
    context = {'address': new_address}
    return render(request, 'address/index.html', context)
