from django.shortcuts import redirect
from django.views import View
from shop_app.models import Product
from .models import FavoriteProduct


class AddToFavorite(View):
    def post(self, request, product_id):
        if 'user_id' in request.session:
            get_product = Product.objects.get(pk=product_id)
            products_slug = get_product.product_slug
            user_id = request.session['user_id']
            new_favorite = FavoriteProduct(
                user_id=user_id,
                product_id=product_id
            )
            new_favorite.save()
            return redirect('shop_app:product_detail', products_slug)

        return redirect('user_app:login')


class RemoveFromFavorites(View):
    def post(self, request, product_id):
        if 'user_id' in request.session:
            user_id = request.session['user_id']
            FavoriteProduct.objects.filter(user_id=user_id, product_id=product_id).delete()
            return redirect('user_app:dashboard')

        return redirect('user_app:login')

