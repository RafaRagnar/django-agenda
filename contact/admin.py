from django.contrib import admin
from contact import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    """ Customization of the Contact model for the Django admin interface. """

    list_display: tuple = ('id', 'first_name', 'last_name', 'phone')
    ordering: tuple = ('-id',)
    list_filter: tuple = ('created_date',)
    search_fields: tuple = ('id', 'first_name', 'last_name')
    list_per_page: int = 15
    list_max_show_all: int = 200
    list_display_links: tuple = ('id', 'first_name')


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Customization of the Category model for the Django admin interface. """
