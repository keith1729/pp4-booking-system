from . import views
from django.urls import path

# URL config
urlpatterns = [
    path('create/', views.CreateAccount.as_view(), name='create_account')
]