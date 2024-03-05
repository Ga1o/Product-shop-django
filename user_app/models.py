from django.db import models


class CustomUser(models.Model):
    user_name = models.CharField('Имя', max_length=200)
    user_email = models.EmailField('Email', unique=True)
    user_password = models.CharField('Пароль', max_length=256)
    user_created = models.DateTimeField('Дата создания', auto_now_add=True)
    user_agreed = models.BooleanField('Согласие', default=False)
    user_activated = models.BooleanField('Активирован', default=False)
    user_banned = models.BooleanField('Забанен', default=False)
    last_login = models.DateTimeField('Последний вход', auto_now=True)

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'
        ordering = ('-user_created',)

    def __str__(self):
        return self.user_name
