from django.urls import path
from . import views

app_name = 'adminlog'

urlpatterns = [
    path('admin-login/', views.admin_login, name='adminlogin'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('view-users/', views.view_users, name='viewusers'),
    path('add-destination/', views.add_destination, name='adddestination'),
    path('view-destinations/', views.view_destinations, name='viewdestinations'),
    path('add-flight/', views.add_flight, name='addflight'),
    path('view-flight/', views.view_flight, name='viewflight'),
    path('all-bookings/', views.all_bookings, name='allbookings'),
    path('feedback/', views.feedback, name='feedback'),
]