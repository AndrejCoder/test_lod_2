# coding: utf-8
from django.db import models


class ViolationRegistry(models.Model):

    violation = models.TextField(verbose_name='Нарушение')
    date = models.DateField(verbose_name='Дата нарушения')
    who = models.CharField(verbose_name='Нарушитель', max_length=255)
