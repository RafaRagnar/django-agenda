from datetime import datetime
from django.db import models
from django.utils import timezone


class Contact(models.Model):
    """ This Class represents a contact with basic information. """

    first_name: str = models.CharField(max_length=50)
    last_name: str = models.CharField(max_length=50, blank=True)
    phone: str = models.CharField(max_length=50)
    email: str = models.EmailField(max_length=254, blank=True)
    created_date: datetime = models.DateTimeField(default=timezone.now)
    description: str = models.TextField(blank=True)
    show: bool = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
