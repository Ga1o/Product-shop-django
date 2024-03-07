from django.db import models


class UserReview(models.Model):
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    review_text = models.TextField(max_length=2000)
    review_data = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'
        index_together = (('id', 'product_id'),)
