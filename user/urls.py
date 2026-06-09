from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('search-flight/', views.search_flight, name='search_flights'),
    path('book-flight/<int:flight_id>/', views.book_flight, name='book_flight'),
    path('payment/<int:booking_id>/', views.payment, name='payment'),
    path('booking-confirm/<int:booking_id>/', views.booking_confirm, name='booking_confirm'),
    path('feedback/', views.feedback, name='feedback'),
    path('profile/', views.profile, name='profile'),
    path('my-bookings/', views.my_bookings, name='mybookings'),

]