from django.urls import path
from . import views

app_name = 'user_app'

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('email_confirm/', views.EmailConfirmView.as_view(), name='email_confirm'),
    path('dashboard/', views.UserDashboardView.as_view(), name='dashboard'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path("cant_enter/", views.CantEnterView.as_view(), name="cant_enter"),
    path('need_activate/', views.UserNeedActivateView.as_view(), name='need_activate'),
    path('forgot_password/', views.UserForgotPasswordView.as_view(), name='forgot_password'),
    path('check_secret_code/', views.CheckSecretCodeView.as_view(), name='check_secret_code'),
    path('check_secret_code_register/', views.CheckSecretCodeViewRegister.as_view(), name='check_secret_code_register'),
    path('new_password/', views.UserNewPasswordView.as_view(), name='new_password'),
]
