from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


# Create your views here.

class RegisterView(CreateView):
    # model = User
    # template_name = 'users/register.html'
    #
    # def get(self, request):

    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    # success_url = reverse_lazy('users:login')
    success_url = reverse_lazy('users:verifyemail')


    def form_valid(self, form):
        self.object = form.save()
        #  self.object
        send_mail(
            subject='Поздравляем с регистрацией',
            message='Вы зарегестрированы',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object.email]
        )
        return super().form_valid(form)

    # , redirect('confirm_email'






class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    # template_name = 'users/register.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class VerifyView(View):
    model = User
    template_name = 'users/register.html'

    def get(self, request):

    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        self.object = form.save()
        #  self.object
        send_mail(
            subject='Поздравляем с регистрацией',
            message='Вы зарегестрированы',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object.email]
        )
        return super().form_valid(form)