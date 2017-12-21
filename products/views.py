from django.shortcuts import render
from .models import Product
from main.models import Category

def product(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(
        request,
        'product/product-detail.html',
        {'categories': Category.objects.all(),
                      'product': product}
    )