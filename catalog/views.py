from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from pytils.translit import slugify

from catalog.forms import *
from catalog.models import *
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
    # success_url = reverse_lazy('catalog:home')

    def get_success_url(self):
        return reverse('catalog:update_product', args=[self.kwargs.get('pk')])

    def get_context_data(self,  **kwargs):

        context_data = super().get_context_data(**kwargs)
        version_formset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = version_formset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = version_formset(instance=self.object)
        #-----------instance=self.object - для редакт, для созд не надо

        return context_data

    def form_valid(self, form):

        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    """страница для удаления Product"""
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

        # item = get_object_or_404(Blog, pk=some_pk)
        # items_table = item.name_table__set.all()
        # image_items = item.name_images_table__set.all()
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

    def get_success_url(self):
        return reverse('catalog:viewblog', args=[self.kwargs.get('pk')])



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

