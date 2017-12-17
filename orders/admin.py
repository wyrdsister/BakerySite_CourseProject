from django.contrib import admin
from orders.models import Status, Order, ProductInOrder

admin.site.register(Status)
admin.site.register(Order)
admin.site.register(ProductInOrder)

