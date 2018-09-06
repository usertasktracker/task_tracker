# coding: utf-8
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=1024)

    class Meta(object):
        db_table = 'user'
        verbose_name = u'Пользователь'
