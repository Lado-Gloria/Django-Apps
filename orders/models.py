from django.db import models

# Create your models here.

class Order(models.Model):
    name = models.CharField(max_length=255)
    orderName = models.CharField(max_length=300)
    orderNumber=models.IntegerField()
    orderTotal =models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
   

    def __str__(self):
        return self.name
    






