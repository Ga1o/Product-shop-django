from django.shortcuts import render
from django.views import View
from shop_app.models import Product, Category
from user_app.models import CustomUser


class Search(View):
    def post(self, request):
        user_request = request.POST.get('user_request')
        search_products = Product.objects.filter(product_name__icontains=user_request)
        if 'user_id' in request.session:
            user_id = request.session['user_id']
            user = CustomUser.objects.get(pk=user_id)
            data = {'products': search_products, 'user': user}
            return render(request, 'search_app/search.html', data)

        data = {'products': search_products, 'user': None}
        return render(request, 'search_app/search.html', data)


class CategorySearch(View):
    def get(self, request, category_slug):
        get_categiry = Category.objects.filter(category_slug=category_slug).first()
        search_products = Product.objects.filter(product_category=get_categiry.id)
        if 'user_id' in request.session:
            user_id = request.session['user_id']
            user = CustomUser.objects.get(pk=user_id)
            data = {'products': search_products, 'user': user}
            return render(request, 'search_app/search.html', data)

        data = {'products': search_products, 'user': None}
        return render(request, 'search_app/search.html', data)
