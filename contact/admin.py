from django.contrib import admin

# Register your models here.
from contact.models import ContactInfo
from contact.v2.models import ContactInfoUpdate

admin.site.register(ContactInfo)
admin.site.register(ContactInfoUpdate)
