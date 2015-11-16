from django.shortcuts import render
from django.http import HttpResponse
from .models import Address


def index(request):
    last_address = Address.objects.last()
    if last_address == None:
        pk = 0
    else:
        pk = last_address.pk
    new_address = Address.create(pk)
    context = {'address': new_address}
    new_address.save()
    return render(request, 'address/index.html', context)
