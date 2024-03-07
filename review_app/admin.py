from django.contrib import admin
from .models import UserReview


@admin.register(UserReview)
class UserReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'product_id', 'review_text', 'review_data')
    list_display_links = ('id', 'user_id')
