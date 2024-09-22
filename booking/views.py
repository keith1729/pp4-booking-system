from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Booking
from .forms import BookingForm
from django.contrib import messages

# Create booking form view


class BookingView(CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'create_booking.html'
    success_url = reverse_lazy('booking_success')

    def form_valid(self, form):
        form.instance.user = self.request.user
        booking = form.save()
        messages.success(self.request, f'Booking Successful! Welcome {self.request.user.username}! Your booking is confirmed for {
                         booking.date} at {booking.time} with {booking.number_of_players} players.')
        return super().form_valid(form)


# def create_booking(request):
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('booking_success')
#     else:
#         form = BookingForm()
#     return render(request, 'booking/create_booking.html', {'form': form})

# # Successful booking view
# def booking_success(request):
#     return render(request, 'booking/booking_success.html')

# # Cancel booking view
# def cancel_booking(request):
#     return render(request, 'booking/cancel_booking.html')
