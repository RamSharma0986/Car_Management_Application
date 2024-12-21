from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Car, CarImage
from .forms import UserRegistrationForm, CarForm, CarImageForm
from django.db.models import Q
from django.contrib import messages  
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                # Show an error if the username already exists
                error_message = "Username already exists, please choose another one."
                return render(request, 'register.html', {'form': form, 'error_message': error_message})
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
        else:
            return render(request, 'register.html', {'form': form})

    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('car_list')
        else:
            # If authentication fails, show an error message
            error_message = "Invalid username or password"
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def car_list(request):
    cars = Car.objects.all()  # List all cars for everyone
    query = request.GET.get('query')
    if query:
        cars = cars.filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(tags__icontains=query))
    return render(request, 'car_list.html', {'cars': cars})


def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'car_detail.html', {'car': car})

# car_create is restricted to logged-in users
@login_required
def car_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.user = request.user
            car.save()
            images = request.FILES.getlist('images')
            for image in images:
                CarImage.objects.create(car=car, image=image)
            return redirect('car_list')
    else:
        form = CarForm()
    return render(request, 'car_create.html', {'form': form})

# car_update is restricted to logged-in users
@login_required
def car_update(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        car_form = CarForm(request.POST, instance=car)
        images = request.FILES.getlist('images')  # Get new images if uploaded
        if car_form.is_valid():
            car_form.save()
            if images:  # Only if new images are uploaded
                # Delete existing images
                car.images.all().delete()  # Use the related name 'images'
                # Save new images
                for image in images:
                    CarImage.objects.create(car=car, image=image)
            return redirect('car_detail', car_id=car.id)
    else:
        car_form = CarForm(instance=car)
    return render(request, 'car_update.html', {'form': car_form, 'car': car})

# car_delete is restricted to logged-in users
@login_required
def car_delete(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.user == car.user:  # Ensure the logged-in user is the car's owner
        car.delete()
    return redirect('car_list')


