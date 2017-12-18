from django.shortcuts import render
from .models import Product

def product(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(
        request,
        'product/product-detail.html',
        locals()
    )