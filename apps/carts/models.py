from django.db import models
from django.contrib.auth import get_user_model

from apps.products.models import Product


User = get_user_model()


class Cart(models.Model):
    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='cart_user',
        verbose_name='пользователь',
    )

    def __str__(self):
        return self.owner.username


class CartItem(models.Model):
    item = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='cart_product',
        verbose_name='продукт',
    )
    telejka = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='cart',
        verbose_name='корзина',
    )
    quantity = models.PositiveIntegerField(
        default=1,
    )

    def __str__(self):
        return self.item.title