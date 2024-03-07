"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls', namespace='main_app')),
    path('', include('user_app.urls', namespace='user_app')),
    path('', include('shop_app.urls', namespace='shop_app')),
    path('', include('favorites_app.urls', namespace='favorites_app')),
    path('', include('review_app.urls', namespace='review_app')),
    path('', include('search_app.urls', namespace='search_app')),
    path('', include('rating_app.urls', namespace='rating_app')),
]


# настройки админки
admin.site.site_header = 'Moя админка'
admin.site.index_title = 'Данные магазина'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

