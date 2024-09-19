from django.urls import path
from .views import RegistrationView
from django.contrib.auth import views as auth_views
from users.forms import LoginForm
from users.views import LoginFormView  

# URL config
urlpatterns = [
    # path('', users_home.as_view(), name='users_home'),
    path('registration/', RegistrationView.as_view(), name='users_registration'),
    path('login/', LoginFormView.as_view(redirect_authenticated_user=True, template_name='users/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]