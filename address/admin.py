from django.contrib import admin
from .models import Address

# Register your models here.
class AddressAdmin(admin.ModelAdmin):
    # Every fields are uneditable so I cannot have fields
    fields = []
    list_display = ('address', 'used', 'creation_date')

admin.site.register(Address, AddressAdmin)
