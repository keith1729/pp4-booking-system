from django.urls import path
from .views import users_home, RegistrationView

# URL config
urlpatterns = [
    path('', users_home.as_view(), name='users_home'),
    path('registration/', RegistrationView.as_view(), name='users_registration'),
]