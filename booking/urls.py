from django.urls import path
from . import views


urlpatterns = [
    path('create_booking/', views.BookingView.as_view(), name='create_booking'),
    path('booking_success/', views.booking_success, name='booking_success'),
    path('my_bookings/', views.BookingListView.as_view(), name='my_bookings'),
    path('edit_booking/<int:pk>/', views.UpdateBookingView.as_view(), name='edit_booking'),
    path('delete_booking/<int:pk>/', views.DeleteBookingView.as_view(), name='delete_booking'),
]
