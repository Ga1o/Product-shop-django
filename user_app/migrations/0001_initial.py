# Generated by Django 5.0.2 on 2024-03-05 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200, verbose_name='Имя')),
                ('user_email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('user_password', models.CharField(max_length=256, verbose_name='Пароль')),
                ('user_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('user_agreed', models.BooleanField(default=False, verbose_name='Согласие')),
                ('user_activated', models.BooleanField(default=False, verbose_name='Активирован')),
                ('user_banned', models.BooleanField(default=False, verbose_name='Забанен')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='Последний вход')),
            ],
            options={
                'verbose_name': 'Пользователи',
                'verbose_name_plural': 'Пользователи',
                'ordering': ('-user_created',),
            },
        ),
    ]
