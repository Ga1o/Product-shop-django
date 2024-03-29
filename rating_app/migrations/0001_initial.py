# Generated by Django 5.0.2 on 2024-03-07 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('rating_value', models.IntegerField()),
                ('rating_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинг',
                'ordering': ('-id',),
                'index_together': {('id', 'product_id', 'user_id')},
            },
        ),
    ]
