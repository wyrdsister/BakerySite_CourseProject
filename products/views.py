from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from .models import Product
from main.models import Category
from .forms import AddProductForm
from cart.cart import Cart


def add_to_cart(request, product_id, quantity):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.add(product, product.price, quantity)


def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)


def get_cart(request):
    return render_to_response('cart.html', {'categories': Category.objects.all(),
                                            'cart': Cart(request),
                                            'user': request.user})


def accept_cart(request, cart_id):
    Cart.clear(cart_id)
    return render_to_response('thanks.html', {'categories': Category.objects.all(),
                                              'user': request.user})


def product(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            count = form.cleaned_data['count']
            add_to_cart(request, product_id, form.cleaned_data['count'])
    else:
        form = AddProductForm()
    return render(
        request,
        'product/product-detail.html',
        {'categories': Category.objects.all(),
         'product': product,
         }
    )
