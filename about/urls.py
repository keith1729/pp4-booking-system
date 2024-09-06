from . import views
from django.urls import path

# URL config
urlpatterns = [
    path('about/', views.AboutPage.as_view(), name='about')
]