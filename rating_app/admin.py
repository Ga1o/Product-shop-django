from django.contrib import admin
from .models import ProductRating


@admin.register(ProductRating)
class ProductRatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_id', 'user_id', 'rating_value', 'rating_added')
    list_display_links = ('id', 'product_id', 'user_id')
