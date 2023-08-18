from django.db import models
from django.utils import timezone


class Post(models.Model):
    """Посты"""
    title = models.CharField("Заголовок", max_length=250)
    description = models.TextField("Описание", max_length=1000)
    date_joined = models.DateTimeField("Дата", default=timezone.now)
    image = models.ImageField("Фото", upload_to='posts', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

