from django import forms
from catalog.models import Product


class ProductCreateForm(forms.ModelForm):

    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('name', 'description', 'image', 'category', 'price', 'date_of_create')
        # exclude =


class ProductUpdateForm(forms.ModelForm):

    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('name', 'description', 'image', 'category', 'price', 'date_of_change')
        # exclude =