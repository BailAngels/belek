from django.urls import path

from apps.categories import views


urlpatterns = [
    path('', views.CategoryListView.as_view(),name='category_index'),
    path('category/detail/<int:pk>/',views.CategoryDetailView.as_view(),name='category_detail'),
]
