from django.contrib import admin
from .models import Payments

# Register your models here.


class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'payment_method','amount', 'total_amount', 'payment_time','payment_date', 'receipt_number', 'status')

  

admin.site.register(Payments, PaymentsAdmin)