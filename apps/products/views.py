from django.views import generic

from apps.products.models import Product


class PrdouctListView(generic.ListView):
    model = Product
    template_name = 'products/index.html'
    context_object_name = 'prdocuts'



class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/detail.html'
    context_object_name = 'products'


