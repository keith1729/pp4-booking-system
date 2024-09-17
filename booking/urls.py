from . import views
from django.urls import path

# URL config
urlpatterns = [
    path('booking/', views.create_booking, name='create_booking'),
    path('success/', views.booking_success, name='booking_success'),
]