from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Category, Review
from django.contrib.auth import logout
from products.models import Product

def home(request):
     categories = Category.objects.all()
     return render(request, 'landing/home.html', { 'categories': categories, 'cat': categories})

def category(request, category_id):
     category = Category.objects.get(id=category_id)
     product_list=Product.objects.filter(category=category_id)
     reviews = Review.objects.all()
     return render(
          request,
          'landing/category-detail.html',
          {
               'category': category,
               'product_list': product_list,
               'cat': Category.objects.all(),
                'reviews': reviews
          }
     )


def about(request):
     return render(request, 'landing/About.html', {'cat': Category.objects.all()})

def contacts(request):
     return render(request, 'landing/contacts.html', {'cat': Category.objects.all()})


def news(request):
     return render(request, 'landing/news.html', {'cat': Category.objects.all()})


def signin(request):
     return render(request, 'registration/signin.html', {'cat': Category.objects.all()})


def signup(request):
     return render(request, 'registration/signup.html', {'cat': Category.objects.all()})

def logout_page(request):
    logout(request)
    return HttpResponseRedirect("/")