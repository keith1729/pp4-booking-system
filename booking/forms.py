from django import forms
from .models import Booking
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user', 'email', 'date', 'time', 'number_of_players']
        widgets = {
            'date': DatePickerInput(format='%Y-%m-%d'),
            'time': TimePickerInput(format='%H:%M:%S'),
        }
