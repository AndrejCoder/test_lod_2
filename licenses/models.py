# coding: utf-8
from django.db import models


class License(models.Model):

    name = models.CharField(verbose_name="Наименование", max_length=255)

    class Meta:
        verbose_name = u'Лицензия'
