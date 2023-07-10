from django.db import models
from inventory.models import Product

class CartItem(models.Model):
    product =models.CharField(max_length=300)
    total =models.IntegerField()
    shiping =models.FloatField()
    addproducts =models.ManyToManyField(Product)
    quantity = models.PositiveIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product
    
