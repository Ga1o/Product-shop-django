from django.db import models


class ProductRating(models.Model):
    product_id = models.IntegerField()
    user_id = models.IntegerField()
    rating_value = models.IntegerField()
    rating_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинг'
        index_together = (('id', 'product_id', 'user_id'),)
  