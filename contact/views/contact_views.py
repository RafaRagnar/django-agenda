''' Contact app views '''
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from contact.models import Contact


def index(request):
    """
    Renders the contact list page.

    This view function handles displaying a paginated list of contacts on the
    homepage or contact index page.
    """
    contacts = Contact.objects.filter(show=True).order_by('-id')[:10]

    print(contacts.query)

    context = {
        'contacts': contacts,
    }
    return render(request, 'contact/index.html', context)


def contact(request, contact_id):
    """
    Renders the details page for a specific contact.

    This view function handles displaying detailed information about a single
    contact based on its ID.
    """
    # single_contact = Contact.objects.filter(pk=contact_id).first()

    # if single_contact is None:
    #     raise Http404()
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)

    context = {
        'contact': single_contact,
    }
    return render(request, 'contact/contact.html', context)
