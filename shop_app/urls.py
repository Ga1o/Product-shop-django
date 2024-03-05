from django.urls import path
from . import views

app_name = 'shop_app'

urlpatterns = [
    path('product_detail/<slug:product_slug>/', views.ProductDetailView.as_view(), name='product_detail'),
]
