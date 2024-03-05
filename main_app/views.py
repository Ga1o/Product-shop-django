from django.shortcuts import render
from django.views import View
from user_app.models import CustomUser
from shop_app.models import Product


class IndexView(View):
    def get(self, request):
        products = Product.objects.all()
        if 'user_id' in request.session:
            user_id = request.session['user_id']
            user = CustomUser.objects.get(pk=user_id)
            data = {'user': user, 'products': products}
            return render(request, 'main_app/index.html', data)

        data = {'user': None, 'products': products}
        return render(request, 'main_app/index.html', data)


class AboutView(View):
    def get(self, request):
        if 'user_id' in request.session:
            user_id = request.session['user_id']
            user = CustomUser.objects.get(pk=user_id)
            data = {'user': user}
            return render(request, 'main_app/about.html', data)

        data = {'user': None}
        return render(request, 'main_app/about.html', data)


class ContactView(View):
    def get(self, request):
        if 'user_id' in request.session:
            user_id = request.session['user_id']
            user = CustomUser.objects.get(pk=user_id)
            data = {'user': user}
            return render(request, 'main_app/contact.html', data)

        data = {'user': None}
        return render(request, 'main_app/contact.html', data)


class RulesView(View):
    def get(self, request):
        if 'user_id' in request.session:
            user_id = request.session['user_id']
            user = CustomUser.objects.get(pk=user_id)
            data = {'user': user}
            return render(request, 'main_app/rules.html', data)

        data = {'user': None}
        return render(request, 'main_app/rules.html', data)
