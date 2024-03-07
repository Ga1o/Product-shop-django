from django.urls import path
from . import views


app_name = 'search_app'

urlpatterns = [
    path('search/', views.Search.as_view(), name='search'),
    path('category_search/<slug:category_slug>/', views.CategorySearch.as_view(), name='category_search'),
]