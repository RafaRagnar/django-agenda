''' Contact app views '''
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from contact.models import Contact


def index(request):
    """
    Renders the contact list page.

    This view function handles displaying a paginated list of contacts on the
    homepage or contact index page.
    """
    contacts = Contact.objects.filter(show=True).order_by('-id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # print(contacts.query)

    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos - '
    }
    return render(request, 'contact/index.html', context)


def search(request):
    """
    Implements a search functionality for contacts based on user input.

    This view function handles searching for contacts based on a query
    string parameter (`q`) and displays the results on the contact list page.
    """
    search_value = request.GET.get('q', '').strip()

    # print('search_value', search_value)

    if search_value == '':
        return redirect('contact:index')

    contacts = Contact.objects.filter(show=True).filter(
        Q(first_name__icontains=search_value) |
        Q(last_name__icontains=search_value) |
        Q(phone__icontains=search_value) |
        Q(email__icontains=search_value)
    ).order_by('-id')

    # print(contacts.query)

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Search - '
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

    site_title = f'{single_contact.first_name} {single_contact.last_name} - '

    context = {
        'contact': single_contact,
        'site_title': site_title,
    }
    return render(request, 'contact/contact.html', context)
