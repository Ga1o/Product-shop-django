from django.urls import path
from . import views

app_name = 'review_app'

urlpatterns = [
    path('add_review/<int:product_id>/', views.AddReview.as_view(), name='add_review'),
    path('remove_review/<int:review_id>/', views.RemoveReview.as_view(), name='remove_review'),
]
