from django.urls import path
from . import views


urlpatterns = [
    path('create_booking/', views.BookingView.as_view(), name='create_booking'),
    path('booking_success/', views.booking_success, name='booking_success'),
]
