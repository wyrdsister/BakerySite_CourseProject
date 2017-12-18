from django.db import models
from main.models import Category
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.PositiveIntegerField(help_text="вес продукта")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='static/media/product_img/')
    image_small = models.ImageField(upload_to='static/media/product_img/', null=True)

    class Meta:
        ordering = ['name', 'price']
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name

class Review(models.Model):
    message = models.TextField(max_length=4000)
    product = models.ForeignKey(Product, related_name='product_review', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_review', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return "Комментарий %s", self.message