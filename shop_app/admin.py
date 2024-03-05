from django.contrib import admin
from .models import Product, Category
from django.utils.safestring import mark_safe


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'show_img', 'product_name', 'product_price', 'product_stock', 'product_available', 'product_created',
    'product_updated')
    list_display_links = ('id', 'show_img', 'product_name')
    list_filter = ('product_available', 'product_created', 'product_updated')
    prepopulated_fields = {'product_slug': ('product_name',)}
    list_per_page = 20

    def get_prepopulated_fields(self, request, obj=None):
        return {
            'product_slug': ('product_name',),
        }

    def show_img(self, obj):
        if obj.product_image:
            return mark_safe('<img src="{}" width="60" />'.format(obj.product_image.url))

    show_img.__name__ = 'Image'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'category_slug')
    ordering = ('id', 'category_name')
    prepopulated_fields = {'category_slug': ('category_name',)}

    def get_prepopulated_fields(self, request, obj=None):
        return {
            'category_slug': ('category_name',),
        }