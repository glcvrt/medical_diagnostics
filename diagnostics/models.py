from django.core.exceptions import ValidationError
from django.db import models
from django.db import models
from django.utils import timezone

from user.models import User

NULLABLE = {'blank': True, 'null': True}


class Directions(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название направления')
    description = models.CharField(max_length=500, verbose_name='Описание', **NULLABLE)
    icon = models.ImageField(upload_to='icons/', verbose_name='Иконка', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'


class Doctor(models.Model):
    fio = models.CharField(max_length=100, verbose_name='ФИО')
    directions = models.ForeignKey(Directions, on_delete=models.CASCADE, verbose_name='Направление')
    experience = models.IntegerField(verbose_name='Стаж')
    add_info = models.CharField(max_length=300, verbose_name='Дополнительная информация')
    timing = models.CharField(verbose_name='Часы приёма', **NULLABLE)

    def __str__(self):
        return f'{self.fio}'

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'


class Diagnostic(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    price = models.PositiveIntegerField(verbose_name='Стоимость')
    doctor = models.ManyToManyField('Doctor', related_name="Врач")

    def __str__(self):
        return f'{self.title}: {self.price}'

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Review(models.Model):
    text = models.CharField(max_length=500, verbose_name='Текст')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пациент', **NULLABLE)

    def __str__(self):
        return f'{self.user} - {self.text}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
