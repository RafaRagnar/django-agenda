""" This module defines models for managing contacts and categories. """
from datetime import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Represents a category for organizing contacts.

    Fields:
        name (str): The name of the category (max. 50 characters).
    """

    class Meta:
        """
        Provides additional configuration options for the Category model.

        verbose_name (str): The singular human-readable name of the model.
            Defaults to the class name with the first letter capitalized
            (e.g., 'Category' in this case).
        verbose_name_plural (str): The plural human-readable name of the model.
            Defaults to adding an 's' to `verbose_name` (e.g., 'Categories').
        """
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name: str = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.name}'


class Contact(models.Model):
    """
    Represents a contact with detailed information.

    Fields:
        first_name (str): The first name of the contact (max. 50 characters).
        last_name (str): The last name of the contact (optional, max. 50 
        characters).
        phone (str): The phone number of the contact (max. 50 characters).
        email (str): The email address of the contact (optional, max. 254
        characters).
        created_date (datetime): The date and time the contact was created
        (defaults to current time).
        description (str): An optional description of the contact.
        show (bool): Whether the contact should be displayed (defaults
        to True).
        picture (ImageField): An optional picture of the contact.
        category (ForeignKey): The category the contact belongs to (optional).
    """

    first_name: str = models.CharField(max_length=50)
    last_name: str = models.CharField(max_length=50, blank=True)
    phone: str = models.CharField(max_length=50)
    email: str = models.EmailField(max_length=254, blank=True)
    created_date: datetime = models.DateTimeField(default=timezone.now)
    description: str = models.TextField(blank=True)
    show: bool = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True)

    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
