# coding: utf-8
from django.db import models


class ViolationRegistry(models.Model):

    violation = models.TextField()
    date = models.DateField()
    who = models.CharField(max_length=255)
