# from django.shortcuts import render, redirect
# from .forms import BookingForm

# # Create booking form view
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
