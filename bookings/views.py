from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class CreateAccount(TemplateView):
    form = UserCreationForm()
    template_name = 'create-account.html'
