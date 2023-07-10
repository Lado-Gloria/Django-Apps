from django.db import models
from inventory .models import Product

class CartItem(models.Model):
    product =models.TextField()
    total =models.IntegerField()
    shiping =models.FloatField()
    addproducts =models.ManyToManyField(Product)
    quantity = models.PositiveIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s cart - {self.product.name}"
