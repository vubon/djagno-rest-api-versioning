from django.db import models


class ContactInfoUpdateManager(models.Manager):

    def v2_data(self):
        return self.all().values()


class ContactInfoUpdate(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(max_length=500, null=True, blank=True)
    secondary_phone = models.CharField(max_length=15, null=True, blank=True)
    objects = ContactInfoUpdateManager()

    def __str__(self):
        return "{}".format(self.name)
