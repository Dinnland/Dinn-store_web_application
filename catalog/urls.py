

from . import views
from django.urls import path
from catalog.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path('', views.redirect_view),

    path('home/', views.index_home, name='home'),
    path('contacts/', views.index_contacts, name='contacts'),
    path('base/', views.base),


]
