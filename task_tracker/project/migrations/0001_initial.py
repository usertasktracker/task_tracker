# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-06 17:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
            ],
            options={
                'db_table': 'project',
                'verbose_name': '\u041f\u0440\u043e\u0435\u043a\u0442',
            },
        ),
    ]
