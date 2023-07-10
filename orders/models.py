from django.db import models
from payment.models import Payments
# from cart.models import CartItem
from customers.models import Customer
from shipment.models import Shipment

class Order(models.Model):
     name = models.CharField(max_length=255)
    #  cart =models.ForeignKey(CartItem, on_delete=models.CASCADE,null=True)
     payment = models.ForeignKey(Payments, on_delete=models.CASCADE, null=True)
     customer =models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
     shipment =models.ForeignKey(Shipment,on_delete=models.CASCADE,null=True)
     orderName = models.CharField(max_length=300)
     orderNumber = models.IntegerField()
     orderTotal = models.IntegerField()
     date_created = models.DateTimeField(auto_now_add=True)
     date_updated = models.DateTimeField(auto_now=True)

     def __str__(self):
        return self.name