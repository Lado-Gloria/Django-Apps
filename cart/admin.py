from django.contrib import admin
from .models import CartItem

# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_display = ('product', 'total','shiping', 'quantity','date_added')

  

admin.site.register(CartItem, CartAdmin)

