# coding: utf-8
from django.db import models


class ProcessType(models.Model):
    name = models.CharField(max_length=255)


class Process(models.Model):
    process_type = models.ForeignKey(
        ProcessType,
        verbose_name=u'Тип процесса',
        db_index=True
    )

    name = models.CharField(max_length=255)
