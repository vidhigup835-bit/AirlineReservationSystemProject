from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from .forms import DestinationForm, FlightForm
from .models import Flight , Destination  
from dashboard.forms import AdminLoginForm
from django.contrib.auth.models import User
from adminlog.models import Booking , Feedback




def admin_login(request):
    form = AdminLoginForm()
    
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None and user.is_staff:
                login(request, user)
                return redirect('adminlog:dashboard')  # ← dashboard pe jayega
            else:
                form.add_error(None, 'Invalid credentials or not an admin!')
    
    return render(request, 'dashboard/adminlogin.html', {'form': form})

def dashboard(request):
    return render(request, 'adminlog/dashboard.html')

def view_users(request):
    users = User.objects.filter(is_staff=False)  # sirf normal users
    return render(request, 'adminlog/view_user.html', {'users': users})



def add_destination(request):
    form = DestinationForm()
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adminlog:viewdestinations')
    return render(request, 'adminlog/add_destination.html', {'form': form})

def view_destinations(request):
    destinations = Destination.objects.all()
    return render(request, 'adminlog/view_destinations.html', {'destinations': destinations})



def add_flight(request):
    form = FlightForm()
    
    if request.method == 'POST':
        form = FlightForm(request.POST, request.FILES)  # ← FILES important hai
        if form.is_valid():
            form.save()
            return redirect('adminlog:viewflight')
    
    return render(request, 'adminlog/addflight.html', {'form': form})


def view_flight(request):
    flights = Flight.objects.all()
    return render(request, 'adminlog/viewflight.html', {'flights': flights})


def all_bookings(request):
    bookings = Booking.objects.all()
    return render(request, 'adminlog/all_bookings.html', {'bookings': bookings})


def feedback(request):
    feedbacks = Feedback.objects.all().order_by('-created_at')
    return render(request, 'adminlog/feedback.html', {'feedbacks': feedbacks})
