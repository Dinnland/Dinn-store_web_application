# from django.contrib.auth.models import User
from django.contrib import auth
from django.forms import inlineformset_factory

from catalog.forms import ProductUpdateFormModerator, ProductUpdateForm, VersionForm
from catalog.models import *
from django_19_hw_2 import settings
from django.core.cache import cache


#


def get_cashed_categories_for_product():
    """КЭШирование для вывода категорий"""

    if settings.CACHE_ENABLED:
        key = 'category_list'
        category_list = cache.get(key)
        if category_list is None:
            category_list = Category.objects.all()
            cache.set(key, category_list)
        else:
            category_list = Category.objects.all()
            return category_list


def get_cashed_versions_for_product(object_pk):
    """КЭШирование для вывода версий"""
    if settings.CACHE_ENABLED:
        key = f'version_list_{object_pk}'
        version_list = cache.get(key)
        if version_list is None:
            version_list = Version.objects.filter(product__pk=object_pk)
            cache.set(key, version_list)
    else:
        version_list = Version.objects.filter(product__pk=object_pk)
    return version_list


def get_filter_user_group(del_group, user):
    """Тут в зависимости от группы юзера выводятся разные формы продукта"""
    if user.groups.filter(name=del_group).exists():
        form_class = ProductUpdateFormModerator
    else:
        form_class = ProductUpdateForm
    return form_class

def get_del_group_for_versions(self_req, del_user, context_data, self):
    """ Тут ТУПО убираем для 'moderator' версии продукта из видимости"""
    if not self_req.user.groups.filter(name=del_user).exists():
        version_formset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self_req.method == 'POST':
            context_data['formset'] = version_formset(self_req.POST, instance=self.object)
        else:
            context_data['formset'] = version_formset(instance=self.object)
    return context_data

