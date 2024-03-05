from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'user_email', 'user_created', 'user_activated', 'user_banned')
    list_display_links = ('id', 'user_name')
    list_per_page = 20
