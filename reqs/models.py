# coding: utf-8
from django.contrib.postgres.fields import JSONField
from django.db import models


class Request(models.Model):

    json_data = JSONField()


class ActivityPlace(models.Model):

    request = models.ForeignKey(Request, verbose_name="Заявление")

    json_data = JSONField()
