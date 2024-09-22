from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Booking
from .forms import BookingForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404


# Create booking form view


class BookingView(CreateView):
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


# def create_booking(request):
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('booking_success')
#     else:
#         form = BookingForm()
#     return render(request, 'booking/create_booking.html', {'form': form})


# # Cancel booking view
# def cancel_booking(request):
#     return render(request, 'booking/cancel_booking.html')
