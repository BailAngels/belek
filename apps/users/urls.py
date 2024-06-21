from django.urls import path

from apps.users import views


urlpatterns = [
    path('register/', views.UserCreateView.as_view(), name='register'),
    path('user/update/<int:pk>/', views.UserUpdateView.as_view(), name='user_update'),
    path('profile/<int:pk>/', views.UserDetailView.as_view(), name='profile'),
]
