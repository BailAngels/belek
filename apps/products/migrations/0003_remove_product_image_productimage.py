# Generated by Django 5.0.6 on 2024-06-28 10:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_product_tag_product_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_image/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prod_img', to='products.product')),
            ],
            options={
                'verbose_name': 'Изображение Продукта',
                'verbose_name_plural': 'Изображения Продуктов',
            },
        ),
    ]
