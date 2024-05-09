from django.db import models
from django.utils import timezone


class Contact(models.Model):
    """ This Class represents a contact with basic information. """

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    created_data = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
