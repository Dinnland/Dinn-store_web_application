

# from catalog.views import redirect_view, ProductListView, ProductDetailView, BlogListView, index_contacts, base, \
#     BlogCreateView, BlogDetailView
# from . import views
from catalog.views import *
from django.urls import path
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', redirect_view),

    path('home/', ProductListView.as_view(extra_context={'title': 'Dinnstore'}), name='home'),
    path('contacts/', index_contacts, name='contacts'),
    path('base/', base),
    path('view/<int:pk>', ProductDetailView.as_view(), name='view'),
    path('createproduct/', ProductCreateView.as_view(), name='create_product'),
    path('updateproduct/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('deleteproduct/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),

    path('createblog/', BlogCreateView.as_view(), name='createblog'),
    path('blog/', BlogListView.as_view(extra_context={'title': 'Dinnstore'}), name='listblog'),
    path('viewblog/<int:pk>/', BlogDetailView.as_view(extra_context={'title': 'Dinnstore'}), name='viewblog'),
    path('editblog/<int:pk>/', BlogUpdateView.as_view(), name='editblog'),
    path('deleteblog/<int:pk>/', BlogDeleteView.as_view(), name='deleteblog'),

]
