# coding: utf-8
from django.db import models

from task_tracker.user.models import User


class Task(models.Model):
    name = models.CharField(max_length=1024)
    status = models.CharField(max_length=1024)
    assignee = models.ForeignKey('user.User', null=True, on_delete=models.CASCADE, related_name='assignee')
    reporter = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='reporter')
    project = models.ForeignKey('project.Project', on_delete=models.CASCADE)

    class Meta(object):
        db_table = 'task'
        verbose_name = u'Задача'


class TaskDescription(models.Model):
    description = models.CharField(max_length=4096)
    task = models.ForeignKey('task.Task', on_delete=models.CASCADE)

    class Meta(object):
        db_table = 'task_description'
        verbose_name = u'Описание задачи'


class TaskComment(models.Model):
    comment = models.CharField(max_length=4096)
    task = models.ForeignKey('task.Task', on_delete=models.CASCADE)

    class Meta(object):
        db_table = 'task_comment'
        verbose_name = u'Комментарий к задачи'