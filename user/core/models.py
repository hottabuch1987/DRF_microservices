from django.db import models
import uuid
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.utils.timesince import timesince


class User(AbstractUser):
    """Пользователь"""

    GENDER_TYPES = (
        ("women", 'женщина'),
        ("men", 'мужчина'),
    )
    STATUS_CHOICES = (
        ('In_active', 'В активном поиске'),
        ('Relationship', 'В отношениях'),
        ('Communication', 'Только Общение'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bio = models.TextField('Описание', max_length=500, blank=True)
    date_joined = models.DateTimeField("Дата регистрации", default=timezone.now)
    birth_date = models.DateField('Дата рождения', null=True, blank=True)
    avatar = models.ImageField("Фото", upload_to='avatars', blank=True, null=True)
    gender = models.CharField("Пол", choices=GENDER_TYPES, max_length=10)
    tel = models.CharField('Телефон', max_length=12)
    status = models.CharField("Статус", max_length=20, choices=STATUS_CHOICES)

    def last_login_formatted(self):
        return timesince(self.last_login)

    def __str__(self):
        return f'{self.username}: {self.first_name} - {self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


