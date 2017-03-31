from django.conf.urls import include, url
from django.contrib import admin
from tastypie.api import Api
from address.api import AddressResource, AdminAddressResource
import settings

v1_api = Api(api_name='v1')
v1_api.register(AddressResource())

admin_api = Api(api_name='admin')
admin_api.register(AdminAddressResource())

urlpatterns = [
    url(r'^$', include('address.urls')),
    url(r'^api/', include(v1_api.urls)),
    url(r'^api/', include(admin_api.urls)),
]

if settings.ADMIN_ENABLED:
    urlpatterns.append(url(r'^admin/', include(admin.site.urls)))
