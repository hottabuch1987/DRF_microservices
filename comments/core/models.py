from django.db import models


class Comment(models.Model):
    """Комментарии"""
    post_id = models.IntegerField()
    text = models.TextField(max_length=1000)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарий'

