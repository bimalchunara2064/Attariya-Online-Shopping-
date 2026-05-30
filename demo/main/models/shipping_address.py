from django.db import models
from django.contrib.auth.models import User


class ShippingAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email= models.EmailField(max_length=300)
    phone_number = models.CharField(max_length=15)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
