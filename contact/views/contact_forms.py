''' Contact app create '''
from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields: tuple = ('first_name', 'last_name', 'phone')

    def clean(self) -> dict[str, Any]:
        cleaned_data = self.cleaned_data

        self.add_error('first_name', ValidationError(
            'Mensagem de erro', code='invalid'))

        self.add_error('first_name', ValidationError(
            'Mensagem de erro 2', code='invalid'))
        return super().clean()


def create(request):
    """

    """

    # print(contacts.query)
    if request.method == 'POST':
        context = {
            'form': ContactForm(request.POST)
        }
        return render(request, 'contact/create.html', context)

    context = {
        'form': ContactForm(request.POST)
    }
    return render(request, 'contact/create.html', context)
