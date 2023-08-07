from django import forms
from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class ProductCreateForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('name', 'description', 'image', 'category', 'price', 'date_of_create')
        # exclude =


class ProductUpdateForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('name', 'description', 'image', 'category', 'price', 'date_of_change')
        # exclude =


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

