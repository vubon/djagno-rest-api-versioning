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

    def __init__(self, *args, **kwargs):
        super(ContactInfo, self).__init__(*args, **kwargs)
        self.old_phone = self.phone

    def save(self, *args, **kwargs):
        if not ContactInfoUpdate.objects.filter(phone=self.old_phone).exists():
            data = dict(name=self.name, phone=self.phone, address=self.address)
            ContactInfoUpdate.objects.create(**data)
        elif not self.old_phone == self.phone:
            ContactInfoUpdate.objects.filter(phone=self.old_phone).update(phone=self.phone)
        # saving data into default database
        super(ContactInfo, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
