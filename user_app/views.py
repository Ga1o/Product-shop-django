from django.shortcuts import render, redirect
from django.views import View
from .models import CustomUser
from favorites_app.models import FavoriteProduct
from shop_app.models import Product
from django.contrib import messages
from .forms import RegisterForm, LoginForm, ForgotPasswordForm, CheckSecretCodeForm, NewPasswordForm
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import logout
from random import randint
from .tasks import send_email_task


class UserLoginView(View):
    def get(self, request):
        if 'user_id' in request.session:
            return redirect('user_app:dashboard')

        form = LoginForm()
        data = {'form': form, 'user': None}
        return render(request, 'user_app/login.html', data)

    def post(self, request):
        form = LoginForm(request.POST)
        data = {'form': form, 'user': None}

        if form.is_valid():
            form_data = form.cleaned_data
            user_email = form_data['user_email']
            user_password = form_data['user_password']

            try:
                user = CustomUser.objects.filter(user_email=user_email).first()
                if user is not None:
                    if check_password(user_password, user.user_password) and user.user_activated == 1:
                        request.session['user_id'] = user.id
                        return redirect('user_app:dashboard')

                    messages.error(request, 'Неверный логин или пароль')
                    return render(request, 'user_app/login.html', data)

                messages.error(request, 'Неверный логин или пароль')
                return render(request, 'user_app/login.html', data)

            except ConnectionError:
                messages.error(request, 'Ошибка авторизации')
                return render(request, 'user_app/login.html', data)

        return render(request, 'user_app/login.html', data)


class UserRegisterView(View):
    def get(self, request):
        if 'user_id' in request.session:
            return redirect('user_app:dashboard')

        form = RegisterForm()
        data = {'form': form, 'user': None}
        return render(request, 'user_app/register.html', data)

    def post(self, request):
        form = RegisterForm(request.POST)
        data = {'form': form, 'user': None}

        if form.is_valid():
            form_data = form.cleaned_data
            user_full_name = form_data['user_full_name']
            user_email = form_data['user_email']
            user_password = form_data['user_password']
            user_password_repeat = form_data['user_password_repeat']

            if len(user_full_name) < 2:
                messages.error(request, 'Слишком короткое мия')
                return render(request, 'user_app/register.html', data)

            if user_password != user_password_repeat:
                messages.error(request, 'Пароли не совпали')
                return render(request, 'user_app/register.html', data)

            if len(user_password) < 1:
                messages.error(request, 'Пароль короткий')
                return render(request, 'user_app/register.html', data)

            try:
                user = CustomUser.objects.filter(user_email=user_email)
                if not user:
                    hashed_password = make_password(user_password)
                    new_user = CustomUser(
                        user_name=user_full_name,
                        user_email=user_email,
                        user_password=hashed_password,
                        user_agreed=form_data['user_agree'],
                    )
                    new_user.save()
                    secret_code = randint(1000, 9999)
                    try:
                        send_email_task.delay('Секретный код', user_email, secret_code)
                        request.session['secret_code'] = secret_code
                        request.session['user_email'] = user_email
                        return redirect('user_app:email_confirm')

                    except Exception as _ex:
                        messages.error(request, 'Ошибка отправки письма')
                        return redirect('user_app:login')

                messages.error(request, 'Email занят')
                return render(request, 'user_app/register.html', data)

            except ConnectionError:
                messages.error(request, 'Ошибка регистрации')
                return render(request, 'user_app/register.html', data)

        return render(request, 'user_app/register.html', data)


class EmailConfirmView(View):
    def get(self, request):
        if 'user_id' in request.session:
            return redirect('user_app:dashboard')

        form = CheckSecretCodeForm()
        data = {'user': None, 'form': form}
        return render(request, 'user_app/email_confirm.html', data)

    def post(self, request):
        secret_code = request.POST.get('secret_code')
        if int(secret_code) == request.session['secret_code']:
            user_email = request.session['user_email']
            CustomUser.objects.filter(user_email=user_email).update(user_activated=True)
            messages.success(request, 'Email подтвержден. Теперь вы можете войти')
            return redirect('user_app:login')

        messages.error(request, 'Код не совпал с тем, что был отрпавлен на email')
        return redirect('user_app:email_confirm')


class CantEnterView(View):
    def get(self, request):
        if 'user_id' in request.session:
            return redirect('user_app:dashboard')

        data = {'user': None}
        return render(request, 'user_app/cant_enter.html', data)


class UserNeedActivateView(View):
    def get(self, request):
        if 'user_id' in request.session:
            return redirect('user_app:dashboard')

        form = ForgotPasswordForm()
        data = {'user': None, 'form': form}
        return render(request, 'user_app/need_activate.html', data)

    def post(self, request):
        user_email = request.POST.get('user_email')
        user = CustomUser.objects.filter(user_email=user_email).first()
        if user is not None:
            secret_code = randint(1000, 9999)
            try:
                send_email_task.delay('Секретный код', user_email, secret_code)
                request.session['secret_code'] = secret_code
                request.session['user_email'] = user_email
                return redirect('user_app:check_secret_code')

            except Exception as _ex:
                messages.error(request, 'Ошибка отправки письма')
                return redirect('user_app:login')

        messages.error(request, 'Пользователь не найден')
        return redirect('user_app:need_activate')


class UserForgotPasswordView(View):
    def get(self, request):
        if 'user_id' in request.session:
            return redirect('user_app:dashboard')

        form = ForgotPasswordForm()
        data = {'form': form, 'user': None}
        return render(request, 'user_app/forgot_password.html', data)

    def post(self, request):
        user_email = request.POST.get('user_email')
        user = CustomUser.objects.filter(user_email=user_email).first()
        if user is not None:
            secret_code = randint(1000, 9999)
            try:
                send_email_task.delay('Секретный код', user_email, secret_code)
                request.session['secret_code'] = secret_code
                request.session['user_email'] = user_email
                return redirect('user_app:check_secret_code_register')

            except Exception as _ex:
                messages.error(request, 'Ошибка отправки письма')
                return redirect('user_app:login')

        messages.error(request, 'Email не найден')
        return redirect('user_app:forgot_password')


class CheckSecretCodeView(View):
    def get(self, request):
        if 'user_id' in request.session:
            return redirect('user_app:dashboard')

        form = CheckSecretCodeForm()
        data = {'user': None, 'form': form}
        return render(request, 'user_app/check_secret_code.html', data)

    def post(self, request):
        secret_code = request.POST.get('secret_code')
        if int(secret_code) == request.session['secret_code']:
            user_email = request.session['user_email']
            CustomUser.objects.filter(user_email=user_email).update(user_activated=True)
            messages.success(request, 'Активация прошла успешно')
            return redirect('user_app:login')

        messages.error(request, 'Неверный код')
        return redirect('user_app:check_secret_code')


class CheckSecretCodeViewRegister(View):
    def get(self, request):
        if 'user_id' in request.session:
            return redirect('user_app:dashboard')

        form = CheckSecretCodeForm()
        data = {'user': None, 'form': form}
        return render(request, 'user_app/check_secret_code.html', data)

    def post(self, request):
        secret_code = request.POST.get('secret_code')
        if int(secret_code) == request.session['secret_code']:
            return redirect('user_app:new_password')

        messages.error(request, 'Неверный код')
        return redirect('user_app:check_secret_code_register')


class UserNewPasswordView(View):
    def get(self, request):
        if 'user_id' in request.session:
            return redirect('user_app:dashboard')

        form = NewPasswordForm()
        data = {'user': None, 'form': form}
        return render(request, 'user_app/new_password.html', data)

    def post(self, request):
        user_password = request.POST.get('new_password')
        user_password_repeat = request.POST.get('new_password_repeat')
        if user_password == user_password_repeat:
            user_email = request.session['user_email']
            CustomUser.objects.filter(user_email=user_email).update(user_password=make_password(user_password))
            messages.success(request, 'Пароль успешно изменен')
            return redirect('user_app:login')

        messages.error(request, 'Пароли не совпали')
        return redirect('user_app:new_password')


class UserDashboardView(View):
    def get(self, request):
        if 'user_id' in request.session:
            user_id = request.session['user_id']
            user = CustomUser.objects.get(pk=user_id)
            favorites_products = FavoriteProduct.objects.filter(user_id=user_id)
            ids = [favorites_product.product_id for favorites_product in favorites_products]
            products = Product.objects.filter(id__in=ids)
            data = {'user': user, 'products': products}
            return render(request, 'user_app/dashboard.html', data)

        return redirect('user_app:login')


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('user_app:login')
