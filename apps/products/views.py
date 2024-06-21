from django.views import generic

from apps.products.models import Product


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'product/detail.html'
    context_object_name = 'products'


