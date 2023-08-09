from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import *
app_name = UsersConfig.name


# class RegistrView:
#     pass


urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('verifyemail/', ProfileView.as_view(template_name='users/verify_email.html'), name='verifyemail'),
    path('verifyemail/<uidb64>/<token>/', VerifyView.as_view(template_name='users/verify_email.html'), name='verifyemail'),

    # verifyemail

]
