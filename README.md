# Airline Reservation System

A comprehensive web-based airline reservation system built with Django. This project allows users to search for flights, make bookings, manage reservations, and provides admin functionalities for managing flights, destinations, and bookings.

## Features

### User Features
- **User Registration & Login**: Secure user authentication
- **Flight Search**: Search flights by destination and travel date
- **Flight Booking**: Book flights with seat selection
- **Booking Management**: View and manage existing bookings
- **Payment Integration**: Online payment processing
- **User Profile**: Manage user information
- **Feedback System**: Submit feedback and reviews
- **About Section**: Learn more about the airline

### Admin Features
- **Admin Dashboard**: Comprehensive admin control panel
- **Flight Management**: Add, edit, and delete flights
- **Destination Management**: Manage flight destinations
- **Booking Overview**: View all user bookings
- **User Management**: Monitor registered users
- **Feedback Review**: View and manage customer feedback

## Project Structure

```
AirlineReservationSystemProject/
├── AirlineReservationSystemProject/    # Main Django project settings
│   ├── settings.py                     # Project configuration
│   ├── urls.py                         # URL routing
│   ├── wsgi.py                         # WSGI configuration
│   └── asgi.py                         # ASGI configuration
├── adminlog/                           # Admin app
│   ├── models.py                       # Admin models
│   ├── views.py                        # Admin views
│   ├── urls.py                         # Admin URL routes
│   └── templates/                      # Admin templates
├── dashboard/                          # Dashboard app
│   ├── models.py                       # Dashboard models
│   ├── views.py                        # Dashboard views
│   ├── urls.py                         # Dashboard URL routes
│   └── templates/                      # Dashboard templates
├── user/                               # User app
│   ├── models.py                       # User models
│   ├── views.py                        # User views
│   ├── urls.py                         # User URL routes
│   └── templates/                      # User templates
├── media/                              # Uploaded files (flights, destinations)
├── manage.py                           # Django management script
└── db.sqlite3                          # SQLite database
```

## Technology Stack

- **Backend**: Django 3.x
- **Database**: SQLite3
- **Frontend**: HTML, CSS, JavaScript
- **Authentication**: Django built-in authentication

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Django 3.x

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR-USERNAME/AirlineReservationSystemProject.git
   cd AirlineReservationSystemProject
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or install Django manually:
   ```bash
   pip install django
   ```

4. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (admin account)**
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create your admin account.

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```
   
   The application will be available at `http://127.0.0.1:8000/`

## Usage

### For Users
- Navigate to the home page
- Register a new account or login
- Search for available flights
- Select and book flights
- Complete payment
- View your bookings in profile
- Submit feedback

### For Admin
- Go to `http://127.0.0.1:8000/admin/` with superuser credentials
- Or navigate to admin dashboard
- Add/edit/delete flights
- Manage destinations
- View all bookings
- Monitor user registrations
- Review customer feedback

## Database Models

### User App
- **User**: Django built-in User model

### Dashboard App
- **UserRegister**: Extended user profile information
- **Flight**: Flight details and pricing
- **Destination**: Flight destinations

### Admin Log App
- **Booking**: User flight bookings
- **BookedSeats**: Selected seats for bookings
- **Feedback**: Customer feedback and reviews

## API Endpoints

### User Routes
- `/user/` - User dashboard
- `/user/search-flights/` - Search flights
- `/user/book-flight/<id>/` - Book a flight
- `/user/my-bookings/` - View bookings
- `/user/profile/` - User profile
- `/user/payment/` - Payment page

### Admin Routes
- `/admin/` - Admin dashboard
- `/admin/add-flight/` - Add new flight
- `/admin/view-flights/` - View all flights
- `/admin/add-destination/` - Add destination
- `/admin/view-destinations/` - View destinations
- `/admin/all-bookings/` - View bookings

## Future Enhancements

- [ ] Email notifications for bookings
- [ ] Multi-currency support
- [ ] Advanced search filters
- [ ] Mobile app
- [ ] Real-time flight availability
- [ ] Refund management system
- [ ] Seat map visualization
- [ ] Integration with payment gateways (Stripe, PayPal)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Author

Vidhi

## Support

For issues or questions, please create an issue on the GitHub repository.

---

**Note**: This is a learning project built for educational purposes. For production use, additional security measures and optimizations are recommended.
