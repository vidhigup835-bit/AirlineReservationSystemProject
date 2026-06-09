from django.db import models
from django.contrib.auth.models import User

class Flight(models.Model):
    company_name = models.CharField(max_length=100)
    flight_name = models.CharField(max_length=100)
    flight_number = models.CharField(max_length=20)
    total_days = models.IntegerField()
    from_city = models.CharField(max_length=100)
    destination_city = models.CharField(max_length=100)
    from_city_arrival_time = models.TimeField()
    from_city_departure_time = models.TimeField()
    destination_arrival_time = models.TimeField()
    destination_departure_time = models.TimeField()
    total_business_seats = models.IntegerField()
    total_economy_seats = models.IntegerField()
    business_fare = models.DecimalField(max_digits=10, decimal_places=2)
    economy_fare = models.DecimalField(max_digits=10, decimal_places=2)
    flight_image = models.ImageField(upload_to='flights/')
    airport_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.flight_number} - {self.from_city} to {self.destination_city}"


class Destination(models.Model):
    city_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default='India')
    airport_name = models.CharField(max_length=100)
    airport_code = models.CharField(max_length=10)
    image = models.ImageField(upload_to='destinations/')
    description = models.TextField()

    def __str__(self):
        return self.city_name


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    seat_type = models.CharField(max_length=20, choices=[
        ('economy', 'Economy'),
        ('business', 'Business')
    ])
    passengers = models.IntegerField(default=1)
    total_fare = models.DecimalField(max_digits=10, decimal_places=2)
    selected_seats = models.CharField(max_length=200, blank=True)  # ← add karo
    booking_date = models.DateTimeField(auto_now_add=True)
    travel_date = models.DateField(null=True, blank=True)


    def __str__(self):
        return f"{self.user.username} - {self.flight.flight_number}"
    

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.subject}"