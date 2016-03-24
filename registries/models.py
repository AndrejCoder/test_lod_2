# coding: utf-8
from django.contrib.postgres.fields import JSONField
from django.db import models


class Registry(models.Model):

    json_data = JSONField()
