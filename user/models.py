import random

from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank':  True, 'null': True}


code = ''.join([str(random.randint(0, 9)) for _ in range(12)])


class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    last_name = models.CharField(max_length=20, verbose_name='Фамилия')
    birthday = models.DateField(verbose_name='Дата рождения')
    email = models.EmailField(unique=True, verbose_name='E-mail')
    telegram = models.CharField(unique=True, max_length=20, verbose_name='Telegram', **NULLABLE)
    phone = models.CharField(unique=True, max_length=20, verbose_name='Номер телефона')
    ver_code = models.CharField(max_length=15, default=code, verbose_name='Проверочный код')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.first_name}'

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'
