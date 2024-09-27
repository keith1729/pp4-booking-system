from django import forms
from .models import Booking
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput
import datetime
from django.utils import timezone


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'time', 'number_of_players']
        widgets = {
            'date': DatePickerInput(format='%Y-%m-%d'),
            'time': TimePickerInput(format='%H:%M:%S'),
        }

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')

        if date and time:
            booking_datetime = timezone.make_aware(
                datetime.datetime.combine(date, time))
            if booking_datetime < timezone.now():
                raise forms.ValidationError(
                    "You cannot book a time in the past!")

        return cleaned_data