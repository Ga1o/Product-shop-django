from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Product
from user_app.models import CustomUser
from review_app.forms import UserReviewForm
from review_app.models import UserReview
from rating_app.models import ProductRating
from cart_app.forms import CartAddProductForm


class ProductDetailView(View):
    def get(self, request, product_slug):
        product = get_object_or_404(Product, product_slug=product_slug)
        cart_product_form = CartAddProductForm()
        review_form = UserReviewForm()
        reviews = UserReview.objects.filter(product_id=product.id)
        users_ids = [review.user_id for review in reviews]
        review_users = CustomUser.objects.filter(id__in=users_ids)

        fact_rating = None
        get_rating = ProductRating.objects.filter(product_id=product.id)

        if get_rating:
            product_ratings = [rating.rating_value for rating in get_rating]
            fact_rating = sum(product_ratings) / len(product_ratings)

        if 'user_id' in request.session:
            user_id = request.session['user_id']
            user = CustomUser.objects.get(pk=user_id)

            data = {'user': user, 'product': product, 'review_form': review_form, 'reviews': reviews,
                    'review_users': review_users, 'fact_rating': fact_rating, 'cart_product_form': cart_product_form}
            return render(request, 'shop_app/product_detail.html', data)

        data = {'user': None, 'product': product, 'review_form': review_form, 'reviews': reviews,
                'review_users': review_users, 'fact_rating': fact_rating, 'cart_product_form': cart_product_form}
        return render(request, 'shop_app/product_detail.html', data)
