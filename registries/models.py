# coding: utf-8
from django.contrib.postgres.fields import JSONField
from django.db import models

from django_rest_json_framework.lookups import KeyValueContains


class Registry(models.Model):

    json_data = JSONField()


JSONField.register_lookup(KeyValueContains)
