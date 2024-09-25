from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Booking
from .forms import BookingForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin


# Create booking form view


class BookingView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'create_booking.html'
    success_url = reverse_lazy('booking_success')

    def form_valid(self, form):
        form.instance.user = self.request.user
        self.object = form.save()
        messages.success(self.request, f'Booking Successful! Welcome {self.request.user.username}! Your booking is confirmed for {
                         self.object.date} at {self.object.time} with {self.object.number_of_players} players.')
        self.request.session['booking_id'] = self.object.id
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['booking'] = self.object
        return context


def booking_success(request):
    booking_id = request.session.get('booking_id')
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'booking_success.html', {'booking': booking})


class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'my_bookings.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


class UpdateBookingView(LoginRequiredMixin, UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'edit_booking.html'
    success_url = reverse_lazy('my_bookings')

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


class DeleteBookingView(DeleteView):
    model = Booking
    template_name = 'delete_booking.html'
    success_url = reverse_lazy('my_bookings')

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)