from django import forms


class RegisterForm(forms.Form):
    user_full_name = forms.CharField(max_length=50, label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Пароль')
    user_password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Повтор пароля')
    user_agree = forms.BooleanField(label='С правилами согласен', widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))


class LoginForm(forms.Form):
    user_email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Пароль')


class CheckSecretCodeForm(forms.Form):
    secret_code = forms.CharField(label='Код', widget=forms.TextInput(attrs={'class': 'form-control'}))


class ForgotPasswordForm(forms.Form):
    user_email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control'}))


class NewPasswordForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Новый пароль')
    new_password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Повтор нового пароля')