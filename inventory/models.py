from django.db import models
from vendors.models import Vendor

class Product(models.Model):
    name = models.CharField(max_length=100)  # Renamed 'names' to 'name'
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name