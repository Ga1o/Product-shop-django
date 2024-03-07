from django.shortcuts import redirect
from django.views import View
from shop_app.models import Product
from .models import UserReview


class AddReview(View):
    def post(self, request, product_id):
        if 'user_id' in request.session:
            get_product = Product.objects.get(pk=product_id)
            product_slug = get_product.product_slug
            create_review = UserReview(
                user_id=request.session['user_id'],
                product_id=product_id,
                review_text=request.POST['review_text']
            )
            create_review.save()
            return redirect('shop_app:product_detail', product_slug)

        return redirect('user_app:login')


class RemoveReview(View):
    def post(self,  request, review_id):
        get_review = UserReview.objects.get(pk=review_id)
        get_product = Product.objects.get(pk=get_review.product_id)
        product_slug = get_product.product_slug
        UserReview.objects.get(pk=review_id).delete()
        return redirect('shop_app:product_detail', product_slug)

