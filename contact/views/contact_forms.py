''' Contact app create '''
from django.shortcuts import render, redirect
from contact.forms import ContactForm


def create(request):
    """

    """

    # print(contacts.query)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        context = {
            'form': form
        }

        if form.is_valid():
            form.save()
            return redirect('contact:create')

        return render(request, 'contact/create.html', context)

    context = {
        'form': ContactForm(request.POST)
    }
    return render(request, 'contact/create.html', context)
