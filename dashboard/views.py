from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login
from .forms import AdminLoginForm
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import RegisterForm
from django.contrib.auth import logout



def home(request):
	"""Render a simple dashboard home page."""
	return render(request, 'dashboard/home.html')
def about(request):
	"""Render a simple about page."""
	return render(request, 'dashboard/about.html')

def adminlogin(request):
    form = AdminLoginForm()
    
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None and user.is_staff:
                auth_login(request, user)
                return redirect('adminlog:dashboard')  # jahan bhejna ho
            else:
                form.add_error(None, 'Invalid credentials or not an admin!')
    
    return render(request, 'dashboard/adminlogin.html', {'form': form})


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            
            # ← Username already exists check karo
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'Username already taken! Choose another.')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=form.cleaned_data['password'],
                    email=form.cleaned_data['email'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                )
                UserProfile.objects.create(
                    user=user,
                    contact=form.cleaned_data['contact'],
                    city=form.cleaned_data['city'],
                    state=form.cleaned_data['state'],
                    country=form.cleaned_data['country'],
                    pincode=form.cleaned_data['pincode'],
                    date_of_birth=form.cleaned_data['date_of_birth'],
                )
                return redirect('dashboard:login')
    
    return render(request, 'dashboard/register.html', {'form': form})



def user_login(request):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('user:home')  # login ke baad home pe jayega
        else:
            error = 'Invalid username or password!'
    
    return render(request, 'dashboard/login.html', {'error': error})



def user_logout(request):
    logout(request)
    return redirect('dashboard:home')
