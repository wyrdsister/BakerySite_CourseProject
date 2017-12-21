from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Status(models.Model):
    name = models.CharField(max_length=15, default="отменен")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

    def __str__(self):
        return "Статус %s", self.name


class Order(models.Model):
    customer_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_order")
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name="status")
    сomments = models.CharField(max_length=450, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return "Заказ %s", self.customer_name


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order")
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name="product_order")
    count_products = models.PositiveIntegerField()
    total_price_items = models.DecimalField(max_digits=10, decimal_places=2) #price*count_product
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Продукт в заказе"
        verbose_name_plural = "Лист продуктов в заказе"

    def __str__(self):
        return "Продукт %s в заказе %s", self.product, self.order

