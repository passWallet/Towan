from django.shortcuts import render
from django.http import HttpResponse
from .models import Address


def index(request):
    last_address = Address.objects.last()
    new_address = Address.create(last_address.pk)
    context = {'address': new_address}
    new_address.save()
    return render(request, 'address/index.html', context)
