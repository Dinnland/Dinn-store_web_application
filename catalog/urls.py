
from django.urls import path, include
# from django.shortcuts import render
from . import views
from catalog.views import index_home

urlpatterns = [
    path('', views.index_contacts, name='index'),
    path('', include('catalog.urls')),
]
