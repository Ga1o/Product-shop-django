from django.contrib import admin
from .models import FavoriteProduct


@admin.register(FavoriteProduct)
class FavoriteProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'product_id', 'data_add', 'data_remove')
    list_display_links = ('id', 'user_id')
