from django.views import generic
from django.contrib.auth import get_user_model

from apps.users import forms

User = get_user_model()


class UserCreateView(generic.CreateView):
    model = User
    form_class = forms.UserCreateForm
    template_name = 'user/register.html'
    success_url = '/'


class UserUpdateView(generic.UpdateView):
    model = User
    form_class = forms.UserUpdateForm
    template_name = 'user/update.html'
    success_url = '/'


class UserDetailView(generic.DetailView):
    model = User
    template_name = 'user/profile.html'
    context_object_name = 'users'
    




