from . import views
from django.urls import path

# URL config
urlpatterns = [
    path('booking/', views.create_booking, name='create_booking'),
    path('success/', views.booking_success, name='booking_success'),
    path('cancel/', views.cancel_booking, name='cancel_booking'),
]