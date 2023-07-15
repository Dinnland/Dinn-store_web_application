from django.shortcuts import render

# Create your views here.


def index_contacts(request):
    context = {'header': 'это header contacts/views.py'}
    return render(request, 'contacts/contacts.html', context)


def index_home(request):
    # context = {'header': 'это header contacts/views.py'}
    return render(request, 'home/home.html')
