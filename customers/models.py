from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=300)
    location = models.CharField(max_length=200)
    email = models.EmailField(max_length=300)
    password = models.CharField(max_length=280)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.name