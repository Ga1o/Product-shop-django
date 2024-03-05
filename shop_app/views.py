from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Product
from user_app.models import CustomUser


class ProductDetailView(View):
    def get(self, request, product_slug):
        product = get_object_or_404(Product, product_slug=product_slug)

        if 'user_id' in request.session:
            user_id = request.session['user_id']
            user = CustomUser.objects.get(pk=user_id)
            data = {'user': user, 'product': product}
            return render(request, 'shop_app/product_detail.html', data)

        data = {'user': None, 'product': product}
        return render(request, 'shop_app/product_detail.html', data)
