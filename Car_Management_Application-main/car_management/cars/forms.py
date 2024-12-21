from django import forms
from django.contrib.auth.models import User
from .models import Car, CarImage

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['title', 'description', 'car_type', 'company', 'dealer', 'tags']

class CarImageForm(forms.ModelForm):
    class Meta:
        model = CarImage
        fields = ['image']
