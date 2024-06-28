from django.shortcuts import get_object_or_404, redirect
from django.views import generic

from apps.carts.models import CartItem, Cart
from apps.carts.forms import CartItemForm
from apps.products.models import Product


class CartDetailView(generic.DetailView):
    model = Cart
    template_name = 'cart/detail.html'
    context_object_name = 'carts'

    def get_object(self):
        cart, created = Cart.objects.get_or_create(owner=self.request.user)


class CartitemCreateView(generic.CreateView):
    model = CartItem
    form_class = CartItemForm
    template_name = 'cart/create.html'

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs['pk'])
        cart, created = Cart.objects.get_or_create(owner=self.request.user)
        cart_item, created = CartItem.objects.get_or_create(item=product, telejka = cart)
        if not created:
            cart_item.quantity += form.cleaned_data['quantity']
        else:
            cart_item.quantity = form.changed_data['quantity']
        cart_item.save()
        return redirect('cart_detail')


class CartItemDeleteView(generic.DeleteView):
    model = CartItem
    template_name = 'cart/delete.html'
    
    def get_queryset(self):
        return CartItem.objects.filter(telejka__owner=self.request.user)
    
    