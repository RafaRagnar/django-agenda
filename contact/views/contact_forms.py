''' Contact app create '''
from django.shortcuts import render
from contact.forms import ContactForm


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
