from django import forms
from cart.cart import Cart
# from orders.models import Order, ProductInOrder

class AddProductForm(forms.Form):
    count = forms.IntegerField(widget=forms.NumberInput)

    class Meta:
        fields = ['count']

