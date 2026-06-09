from django.contrib import admin
from .models import Flight

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ['flight_number', 'company_name', 'from_city', 'destination_city', 'economy_fare']
    search_fields = ['flight_number', 'from_city', 'destination_city']