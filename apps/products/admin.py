from django.contrib import admin

from apps.products.models import Product, ProductImage


class ProductInLine(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
    search_fields = ['title']
    inlines = [ProductInLine]


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['image']