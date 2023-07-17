from django.shortcuts import render

# Create your views here.


def index_contacts(request):
    context = {'header': 'это header contacts/views.py'}
    return render(request, 'catalog/contacts.html', context)


def index_home(request):
    # context = {'header': 'это header contacts/views.py'}
    return render(request, 'catalog/home.html')


def index_home2(request):
    # context = {'header': 'это header contacts/views.py'}
    return render(request, 'home/catalog.html')


# def index_main(request):
#     # context = {'header': 'это header contacts/views.py'}
#     return render(request, 'catalog/index.html')
