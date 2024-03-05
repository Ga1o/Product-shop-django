from django.db import models


class FavoriteProduct(models.Model):
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    data_add = models.DateTimeField(auto_now_add=True)
    data_remove = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Избранные'
        verbose_name_plural = 'Избранные'
        index_together = (('id', 'user_id', 'product_id'),)

