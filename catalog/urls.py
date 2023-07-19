

from . import views
from django.urls import path


urlpatterns = [
    path('', views.index_home),
    path('contacts/', views.index_contacts),
    path('home/', views.index_home),
    path('home2/', views.index_home2),

]
