from django import forms 

from apps.carts.models import CartItem


class CartItemForm(forms.ModelForm):

    class Meta:
        model = CartItem
        fields = ['quantity']

