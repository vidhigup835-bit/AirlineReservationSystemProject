from django import forms
from .models import Flight , Destination

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = '__all__'
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control admin-input', 'placeholder': 'Enter Company Name'}),
            'flight_name': forms.TextInput(attrs={'class': 'form-control admin-input', 'placeholder': 'Enter Flight Name'}),
            'flight_number': forms.TextInput(attrs={'class': 'form-control admin-input', 'placeholder': 'Enter Flight Number'}),
            'total_days': forms.NumberInput(attrs={'class': 'form-control admin-input', 'placeholder': 'Enter Total Days'}),
            'from_city': forms.TextInput(attrs={'class': 'form-control admin-input', 'placeholder': 'Enter From City'}),
            'destination_city': forms.TextInput(attrs={'class': 'form-control admin-input', 'placeholder': 'Enter Destination City'}),
            'from_city_arrival_time': forms.TimeInput(attrs={'class': 'form-control admin-input', 'type': 'time'}),
            'from_city_departure_time': forms.TimeInput(attrs={'class': 'form-control admin-input', 'type': 'time'}),
            'destination_arrival_time': forms.TimeInput(attrs={'class': 'form-control admin-input', 'type': 'time'}),
            'destination_departure_time': forms.TimeInput(attrs={'class': 'form-control admin-input', 'type': 'time'}),
            'total_business_seats': forms.NumberInput(attrs={'class': 'form-control admin-input', 'placeholder': 'Enter Business Seats'}),
            'total_economy_seats': forms.NumberInput(attrs={'class': 'form-control admin-input', 'placeholder': 'Enter Economic Seats'}),
            'business_fare': forms.NumberInput(attrs={'class': 'form-control admin-input', 'placeholder': 'Enter Fare'}),
            'economy_fare': forms.NumberInput(attrs={'class': 'form-control admin-input', 'placeholder': 'Enter Fare'}),
            'flight_image': forms.ClearableFileInput(attrs={'class': 'form-control admin-input'}),
            'airport_name': forms.TextInput(attrs={'class': 'form-control admin-input', 'placeholder': 'Enter Airport Name'}),
        }


class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = '__all__'
        widgets = {
            'city_name': forms.TextInput(attrs={'class': 'form-control admin-input', 'placeholder': 'e.g. Mumbai'}),
            'country': forms.TextInput(attrs={'class': 'form-control admin-input', 'placeholder': 'e.g. India'}),
            'airport_name': forms.TextInput(attrs={'class': 'form-control admin-input', 'placeholder': 'e.g. Chhatrapati Shivaji Airport'}),
            'airport_code': forms.TextInput(attrs={'class': 'form-control admin-input', 'placeholder': 'e.g. BOM'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control admin-input'}),
            'description': forms.Textarea(attrs={'class': 'form-control admin-input', 'rows': 3, 'placeholder': 'City description...'}),
        }