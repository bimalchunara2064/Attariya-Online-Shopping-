from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} {self.last_name} - {self.email} {self.phone}  {self.message}"