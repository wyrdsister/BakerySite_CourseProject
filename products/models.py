from django.db import models
from main.models import Category
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=4000, help_text="подробное описание продукта")
    small_description = models.TextField(max_length=250, help_text="краткое описание продукта")
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.PositiveIntegerField(help_text="вес продукта")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='product_img/', null=True)
    image_small = models.ImageField(upload_to='product_img_small/', null=True)

    class Meta:
        ordering = ['name', 'price']
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name