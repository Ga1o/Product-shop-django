# Generated by Django 5.0.2 on 2024-03-05 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('product_id', models.IntegerField()),
                ('data_add', models.DateTimeField(auto_now_add=True)),
                ('data_remove', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Избранные',
                'verbose_name_plural': 'Избранные',
                'ordering': ('-id',),
                'index_together': {('id', 'user_id', 'product_id')},
            },
        ),
    ]