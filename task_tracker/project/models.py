# coding: utf-8
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=1024)

    class Meta(object):
        db_table = 'project'
        verbose_name = u'Проект'

