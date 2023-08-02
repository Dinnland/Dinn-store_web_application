from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify

from catalog.forms import *
from catalog.models import Product, Blog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here. контроллеры


def redirect_view(request):
    """перенаправляет урл сразу на /home/"""
    response = redirect('/home/')
    return response


def base(request):
    """ Базовый шаблон с меню, футером и тд """
    context = {'title': 'Dinnland'}
    return render(request, 'catalog/base.html', context)


def index_contacts(request):
    """Стр с контактами"""
    context = {
        'header': 'Контакты'
               }
    return render(request, 'catalog/contacts.html', context)


class ProductListView(ListView):
    """Главная стр с продуктами"""
    model = Product
    template_name = 'catalog/home.html'


class ProductDetailView(DetailView):
    """ стр с продуктами"""
    model = Product
    template_name = 'catalog/product_detail.html'


class ProductCreateView(CreateView):
    """страница для создания продукта"""
    model = Product
    form_class = ProductCreateForm
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    """страница для Изменения продукта"""
    model = Product
    form_class = ProductUpdateForm
    success_url = reverse_lazy('catalog:home')


class ProductDeleteView(DeleteView):
    """страница для удаления блога"""
    model = Product
    # fields = ('__all__')
    # fields = ('header', 'content', 'image')
    success_url = reverse_lazy('catalog:home')


# Блог
class BlogCreateView(CreateView):
    """страница для создания блога"""
    model = Blog
    # fields = ('__all__')
    fields = ('header', "slug", 'content', 'image', 'date_of_create')
    success_url = reverse_lazy('catalog:listblog')

    def form_valid(self, form):
        """динамическое формирование Slug"""
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.header)
            new_blog.save()
        return super().form_valid(form)


class BlogListView(ListView):
    """ Главная стр с блогами"""
    model = Blog

    def get_queryset(self, queryset=None, *args, **kwargs):
        """Метод для вывода ТОЛЬКО опубликованных блогов"""
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(sign_of_publication=True)
        return queryset


class BlogDetailView(DetailView):
    """Стр с блогом"""
    model = Blog

    def get_object(self, queryset=None):
        """Метод для подсчета просмотров"""
        self.object = super().get_object(queryset)
        self.object.quantity_of_views += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    """страница для Изменения блога"""
    model = Blog
    # fields = ('__all__')
    fields = ('header', 'content', 'image')
    # success_url = reverse_lazy('catalog:listblog')

    def form_valid(self, form):
        """динамическое формирование Slug"""
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.header)
            new_blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:viewblog', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    """страница для удаления блога"""
    model = Blog
    # fields = ('__all__')
    # fields = ('header', 'content', 'image')
    success_url = reverse_lazy('catalog:listblog')

