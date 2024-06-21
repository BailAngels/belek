from django.urls import path

from apps.products import views


urlpatterns = [
    path('detail/<int:pk>/',views.ProductDetailView.as_view(),name='detail'),
]
