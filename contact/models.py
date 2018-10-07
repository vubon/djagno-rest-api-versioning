from django.db import models

from contact.v2.models import ContactInfoUpdate


class ContactManager(models.Manager):

    def v1_data(self):
        return self.all().values()


# Create your models here.
class ContactInfo(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField(max_length=500)

    objects = ContactManager()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        data = dict(name=self.name, phone=self.phone, address=self.address)
        if not ContactInfoUpdate.objects.filter(**data).exists():
            ContactInfoUpdate.objects.create(**data)
        print(update_fields)
        # saving data into default database
        super(ContactInfo, self).save(using='default')

    def __str__(self):
        return self.name
