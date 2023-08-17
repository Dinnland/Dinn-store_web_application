from catalog.models import *
from django_19_hw_2 import settings
from django.core.cache import cache


def category_selection(model):
    """выюорка категорий, или чего угодно"""
    the_model = model
    category_select = the_model.objects.all()
    return category_select


def get_cashed_categories_for_product(object_pk):
    """КЭШирование для вывода версий"""
    # # context_data = super().get_context_data(**kwargs)
    # # associated_field = associated_field
    # if settings.CACHE_ENABLED:
    #     # key = f'version_list_{self.object.pk}'
    #     key = key
    #     version_list = cache.get(key)
    #     if version_list is None:
    #         version_list = associated_field
    #         cache.set(key, version_list)
    # else:
    #     version_list = associated_field
    # # context_data['versions'] = self.object.product_versions.all()
    # context_data['versions'] = version_list
    # return context_data
    if settings.CACHE_ENABLED:
        key = f'category_list_{object_pk}'
        category_list = cache.get(key)
        if category_list is None:
            # version_list = associated_field
            category_list = Product.objects.filter(product__pk=object_pk)

            cache.set(key, category_list)
    else:
        # version_list = self.object.product_versions.all()
        category_list = Product.objects.filter(product__pk=object_pk)
    return category_list



def get_cashed_versions_for_product(object_pk):
    if settings.CACHE_ENABLED:
        key = f'version_list_{object_pk}'
        version_list = cache.get(key)
        if version_list is None:
            # version_list = associated_field
            version_list = Product.objects.filter(product__pk=object_pk)

            cache.set(key, version_list)
    else:
        # version_list = self.object.product_versions.all()
        version_list = Product.objects.filter(product__pk=object_pk)
    return version_list
