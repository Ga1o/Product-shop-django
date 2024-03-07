from django.urls import path
from . import views

app_name = 'rating_app'

urlpatterns = [
    path('add_rating/<int:product_id>/<int:rating_value>', views.AddRatingProduct.as_view(), name='add_rating'),
]
