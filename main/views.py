from django.shortcuts import render
from .models import Category
from products.models import Product

def landing(request):
     return render(request, 'landing/landing.html', locals())


def home(request):
     categories = Category.objects.all()
     return render(request, 'landing/home.html', locals())

def category(request, category_id):
     category = Category.objects.get(id=category_id)
     product_list=Product.objects.filter(category=category_id)
     return render(
          request,
          'landing/category-detail.html',
          locals()
     )