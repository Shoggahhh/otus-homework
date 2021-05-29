from django.shortcuts import render
from django.views.generic import CreateView
from userapp.models import MyUser
from userapp.forms import RegisterForm
from django.contrib.auth.views import LoginView

# Create your views here.
class RegisterView(CreateView):
    model = MyUser
    form_class = RegisterForm
    template_name = 'userapp/register.html'
    success_url = 'ticket_list/'


class AuthView(LoginView):
    template_name = 'userapp/login.html'
    success_url = 'helpapp/ticket_list.html'