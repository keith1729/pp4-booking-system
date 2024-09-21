# from django.shortcuts import render, redirect
# from django.views import View
# from django.contrib import messages
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.views import LoginView
# from .forms import RegistrationForm, LoginForm

# Create your views here.
# class RegistrationView(View):
#     form_class = RegistrationForm
#     initial = {'key': 'value'}
#     template_name = 'users/registration.html'

#     def dispatch(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return redirect(to='login')

#         return super(RegistrationView, self).dispatch(request, *args, **kwargs)

#     def get(self, request, *args, **kwargs):
#         form = self.form_class(initial=self.initial)
#         return render(request, self.template_name, {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)

#         if form.is_valid():
#             form.save()

#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}')

#             return redirect(to='login')

#         return render(request, self.template_name, {'form': form})

    
# class LoginFormView(LoginView):
#     form_class = LoginForm

#     def form_valid(self, form):
#         remember_me = form.cleaned_data.get('remember_me')

#         if not remember_me:
#             self.request.session.set_expiry(0)
#             self.request.session.modified = True

#         return super(LoginFormView, self).form_valid(form)