from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Product
from user_app.models import CustomUser
from review_app.forms import UserReviewForm
from review_app.models import UserReview


class ProductDetailView(View):
    def get(self, request, product_slug):
        product = get_object_or_404(Product, product_slug=product_slug)

        review_form = UserReviewForm()
        reviews = UserReview.objects.filter(product_id=product.id)
        users_ids = [review.user_id for review in reviews]
        review_users = CustomUser.objects.filter(id__in=users_ids)

        if 'user_id' in request.session:
            user_id = request.session['user_id']
            user = CustomUser.objects.get(pk=user_id)

            data = {'user': user, 'product': product, 'review_form': review_form, 'reviews': reviews,
                    'review_users': review_users}

            return render(request, 'shop_app/product_detail.html', data)

        data = {'user': None, 'product': product, 'review_form': review_form, 'reviews': reviews,
                'review_users': review_users}

        return render(request, 'shop_app/product_detail.html', data)
