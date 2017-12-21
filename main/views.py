from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .models import Category, Review
from django.contrib.auth import logout
from products.models import Product
from .forms import NewReviewForm, SignUpForm
from django.contrib.auth import login as auth_login


def home(request):
    categories = Category.objects.all()
    if request.method == "POST":
        form = NewReviewForm(request.POST)
        if form.is_valid():
            Review.objects.create(message=form.cleaned_data['message'], ownuser=request.user)
    else:
        form = NewReviewForm()
    reviews = Review.objects.all()
    return render(request, 'landing/home.html', {'categories': categories,
                                                 'cat': categories,
                                                 'reviews': reviews,
                                                 'form': form})


def category(request, category_id):
    category = Category.objects.get(id=category_id)
    product_list = Product.objects.filter(category=category_id)
    return render(
        request,
        'landing/category-detail.html',
        {
            'category': category,
            'product_list': product_list,
            'cat': Category.objects.all(),
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
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'cat': Category.objects.all(), 'form': form})


@login_required
def logout_page(request):
    logout(request)
    return HttpResponseRedirect("/")
