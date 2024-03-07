from django.shortcuts import redirect
from django.views import View
from .models import ProductRating
from shop_app.models import Product


class AddRatingProduct(View):
    def get(self, request, product_id, rating_value):
        if 'user_id' not in request.session:
            return redirect('user_app:login')

        check_rating = ProductRating.objects.filter(user_id = request.session['user_id'],product_id = product_id).first()

        if not check_rating:
            new_rating = ProductRating(
                user_id = request.session['user_id'],
                product_id=product_id,
                rating_value=rating_value
            )
            new_rating.save()

            get_product = Product.objects.get(pk=product_id)
            return redirect('shop_app:product_detail', get_product.product_slug)
        
        get_product = Product.objects.get(pk=product_id)
        return redirect('shop_app:product_detail', get_product.product_slug)
    