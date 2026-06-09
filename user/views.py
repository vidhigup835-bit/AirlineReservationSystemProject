from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from adminlog.models import Flight, Booking , Feedback
from datetime import date
from dashboard.models import UserProfile





@login_required(login_url='dashboard:login')
def home(request):
    return render(request, 'user/home.html')


@login_required(login_url='dashboard:login')
def search_flight(request):
    from_cities = Flight.objects.values_list('from_city', flat=True).distinct()
    to_cities = Flight.objects.values_list('destination_city', flat=True).distinct()
    flights = None

    if request.method == 'POST':
        from_city = request.POST.get('from_city')
        to_city = request.POST.get('to_city')
        flights = Flight.objects.filter(
            from_city__icontains=from_city,
            destination_city__icontains=to_city
        )

    return render(request, 'user/search_flights.html', {
        'flights': flights,
        'from_cities': from_cities,
        'to_cities': to_cities,
    })

@login_required(login_url='dashboard:login')
def book_flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    booked_seats = Booking.objects.filter(flight=flight).values_list('selected_seats', flat=True)
    booked_seat_list = []
    for s in booked_seats:
        if s:
            booked_seat_list.extend(s.split(','))

    # Economy rows — 25 rows, A B C D E F
    economy_rows = []
    for r in range(1, 26):
        row = []
        for col in ['A', 'B', 'C', 'D', 'E', 'F']:
            seat_name = f"E{r}{col}"
            row.append({'name': seat_name, 'booked': seat_name in booked_seat_list})
        economy_rows.append(row)

    # Business rows — 3 rows, A B C D E F
    business_rows = []
    for r in range(1, 4):
        row = []
        for col in ['A', 'B', 'C', 'D', 'E', 'F']:
            seat_name = f"B{r}{col}"
            row.append({'name': seat_name, 'booked': seat_name in booked_seat_list})
        business_rows.append(row)

    if request.method == 'POST':
        seat_type = request.POST.get('seat_type')
        passengers = int(request.POST.get('passengers', 0))
        selected_seats = request.POST.get('selected_seats', '')

        if seat_type == 'economy':
            fare = flight.economy_fare * passengers
        else:
            fare = flight.business_fare * passengers

        booking = Booking.objects.create(
            user=request.user,
            flight=flight,
            seat_type=seat_type,
            passengers=passengers,
            total_fare=fare,
            selected_seats=selected_seats,
            travel_date=request.POST.get('travel_date'),  
        )

        return redirect('user:payment' , booking_id=booking.id)
    return render(request, 'user/book_flight.html', {
        'flight': flight,
        'economy_rows': economy_rows,
        'business_rows': business_rows,
        'today': date.today(),
    })


@login_required(login_url='dashboard:login')
def payment(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    
    if request.method == 'POST':
        # Payment successful — confirmation page pe bhejo
        return redirect('user:booking_confirm', booking_id=booking.id)
    
    return render(request, 'user/payment.html', {'booking': booking})

@login_required(login_url='dashboard:login')
def booking_confirm(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'user/booking_confirm.html', {'booking': booking})


@login_required(login_url='dashboard:login')
def feedback(request):
    success = False
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Feedback.objects.create(
            user=request.user,
            subject=subject,
            message=message,
        )
        success = True
    return render(request, 'user/feedback.html', {'success': success})


@login_required(login_url='dashboard:login')
def profile(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except:
        profile = None
    return render(request, 'user/profile.html', {'profile': profile})

@login_required(login_url='dashboard:login')
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'user/my_bookings.html', {'bookings': bookings})
