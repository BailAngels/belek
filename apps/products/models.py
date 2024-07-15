from django.db import models
import os


from apps.categories.models import Category

class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='category',
        verbose_name='Категория',
    )
    title = models.CharField(
        max_length=150,
        verbose_name='Название',
    )
    description = models.TextField(
        verbose_name='Описание',
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата',
    )

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ProductImage(models.Model):
    image = models.ImageField(
        upload_to='product_image/',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='prod_img'
    )

    def delete(self, usign=None, keep_parents=False):
        os.remove(self.image.path)
        super().delete(using=None, keep_parents=False)

    def __str__(self):
        return self.image.path
    
    class Meta:
        verbose_name="Изображение Продукта"
        verbose_name_plural = "Изображения Продуктов"

