# Generated by Django 5.0.2 on 2024-03-07 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('product_id', models.IntegerField()),
                ('review_text', models.TextField(max_length=2000)),
                ('review_data', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Отзывы',
                'verbose_name_plural': 'Отзывы',
                'ordering': ('-id',),
                'index_together': {('id', 'product_id')},
            },
        ),
    ]
