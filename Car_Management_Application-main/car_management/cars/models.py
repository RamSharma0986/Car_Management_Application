from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    car_type = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    dealer = models.CharField(max_length=50)
    tags = models.CharField(max_length=200)  
    def __str__(self):
        return self.title

class CarImage(models.Model):
    car = models.ForeignKey(Car, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='car_images/')

    def __str__(self):
        return f"Image for {self.car.title}"
