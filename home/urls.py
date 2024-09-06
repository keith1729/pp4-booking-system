from . import views
from django.urls import path

# URL config
urlpatterns = [
    path('', views.HomePage.as_view(), name='home')
]