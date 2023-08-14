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

    all_fields = ('__all__',)

    all_fields_my = ('name', 'description', 'image', 'category', 'price', 'date_of_create', 'date_of_change', 'owner', 'sign_of_publication',)
    moderator_fields = ('sign_of_publication', 'description', 'category',)
    moderator_readonly_fields = ('name', 'image', 'price', 'date_of_create', 'date_of_change', 'owner',)
    my_readonly_fields = ('name',)

    readonly_fields = all_fields_my
    # # Тут мы можем скрывать поля-атрибуты в зависимости от группы пользователя для админки
    # def get_fieldsets(self, request, obj=None, **kwargs):
    #     for group in request.user.groups.all():
    #         if str(group) == 'moderator':
    #             # if request.user.username == 'example@example.com':
    #                 # self.fields = self.available_fields + self.hidden_fields
    #             self.fields = ('sign_of_publication', 'description', 'category',)
    #             # self.fields = self.available_fields
    #             self.readonly_fields = self.my_readonly_fields
    #         else:
    #             self.fields  = ('__all__',)
    #     return super(ProductAdmin, self).get_form(request, obj, **kwargs)



    def get_readonly_fields(self, request, obj=None):
        """Данный метод отдает кортеж с элементами только для чтения"""
        if request.user.groups.filter(name='moderator').exists():
            return self.moderator_readonly_fields

        else:
            return super(ProductAdmin, self).get_readonly_fields(request, obj=obj)





    # def get_readonly_fields(self, request, obj=None):
    #     # if obj:
    #     for group in request.user.groups.all():
    #         if str(group) == 'moderator':
    #             return ['sign_of_publication', 'description',]



@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'version_number', 'version_name', 'sign_of_current_version')
    list_filter = ('version_name',)
    search_fields = ('product', 'version_number', 'version_name')
