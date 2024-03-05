from django.urls import path
from . import views

app_name = 'favorites_app'

urlpatterns = [
    path('add_to_favorite/<int:product_id>', views.AddToFavorite.as_view(), name='add_to_favorite'),
    path('remove_from_favorites/<int:product_id>', views.RemoveFromFavorites.as_view(), name='remove_from_favorites'),
]