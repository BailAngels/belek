from django.views import generic

from apps.categories.models import Category


class CategoryListView(generic.ListView):
    model = Category
    template_name = 'category/index.html'
    context_object_name = 'categories'


class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'category/detail.html'
    context_object_name = 'categories'

    
