from django.contrib import admin
from .models import *

# class ProductAdmin(admin.ModelAdmin):
#     list_display = []

admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)