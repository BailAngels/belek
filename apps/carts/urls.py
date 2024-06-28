from django.urls import path

from apps.carts import views

urlpatterns = [
    path('cart/detail/<int:pk>/', views.CartDetailView.as_view(), name='cart_detail'),
    path('item/create/', views.CartitemCreateView.as_view(), name='item_create'),
    path('item/delete/<int:pk>/', views.CartItemDeleteView.as_view(), name='item_delete'),
]
