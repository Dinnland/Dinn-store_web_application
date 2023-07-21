from django.shortcuts import render
from django.shortcuts import redirect

from catalog.models import Product

# Create your views here. контроллеры


def index_contacts(request):
    context = {
        'header': 'Контакты'
               }
    return render(request, 'catalog/contacts.html', context)


def redirect_view(request):
    # перенаправляет урл сразу на /home/
    response = redirect('/home/')
    return response


def index_home(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Главная'
    }
    return render(request, 'catalog/home.html', context)


def base(request):
    return render(request, 'catalog/base.html')