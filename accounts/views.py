from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import RegisterForm
from django.urls import reverse_lazy

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Login Successful! Welcome {user.username}!')
            return redirect('home')
        else:
            messages.success(request, 'There was an error logging in! Please try again...')
            return redirect('login')
    
    else:
        return render(request, 'login.html', {})


class HomeView(TemplateView):
    template_name = 'home.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, f'Registration Successful! Welcome {user.username}!')
        return super().form_valid(form)




