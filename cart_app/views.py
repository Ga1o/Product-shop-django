from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop_app.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from user_app.models import CustomUser


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart_app:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_app:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'update': True
        })

    user = None    
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        user = CustomUser.objects.get(pk=user_id)
    
    data = {'cart': cart, 'user': user}    
    return render(request, 'cart_app/detail.html', data)


