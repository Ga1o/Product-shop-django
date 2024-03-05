from django.db import models
from django.utils.text import slugify
import random
import string
from django.urls import reverse


class Product(models.Model):
    product_name = models.CharField('Название', max_length=200, db_index=True)
    product_slug = models.SlugField('URL', max_length=200, unique=True, db_index=True)
    product_brand = models.CharField('Бренд', max_length=200)
    product_price = models.IntegerField('Цена')
    product_desc = models.TextField('Описание', max_length=2000)
    product_image = models.ImageField('Изображение', upload_to='product_images/')
    product_available = models.BooleanField('Наличие', default=True)
    product_stock = models.PositiveIntegerField('Количество', default=0)
    product_created = models.DateTimeField('Дата добавления', auto_now_add=True)
    product_updated = models.DateTimeField('Дата обновления', auto_now=True)
    product_category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        index_together = (('id', 'product_slug'),)
        ordering = ('-product_created',)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('shop_app:product_detail', kwargs={'product_slug': self.product_slug})


class ProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(product_available=True)


class ProductProxy(Product):
    objects = ProductManager()

    class Meta:
        proxy = True


def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


class Category(models.Model):
    category_name = models.CharField('Категория', max_length=200, db_index=True)
    category_parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                                        related_name='children')
    category_slug = models.SlugField('URL', max_length=200, unique=True, editable=True, null=False)
    category_created = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        unique_together = (['category_slug', 'category_parent'])
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        full_path = [self.category_name]
        k = self.category_parent
        while k is not None:
            full_path.append(k.category_name)
            k = k.category_parent

        return ' -> '.join(full_path[::-1])

    def save(self, *args, **kwargs):
        if not self.category_slug:
            self.category_slug = slugify(rand_slug() + '-pickBetter' + self.category_name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('model_detail', kwargs={'pk': self.pk})
