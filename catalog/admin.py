from django.contrib import admin
from catalog.models import *

# Register your models here.
# admin.site.register(Category)
# admin.site.register(Product)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'version_number', 'version_name', 'sign_of_current_version')
    list_filter = ('version_name',)
    search_fields = ('product', 'version_number', 'version_name')
