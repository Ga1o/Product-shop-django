from django.urls import path
from . import views

app_name = 'main_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('rules/', views.RulesView.as_view(), name='rules'),
]
