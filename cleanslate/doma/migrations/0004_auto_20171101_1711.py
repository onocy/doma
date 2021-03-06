# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 21:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doma', '0003_auto_20171101_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='createdBy',
        ),
        migrations.RemoveField(
            model_name='village',
            name='home',
        ),
        migrations.AddField(
            model_name='home',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='home_created_by', to='doma.User'),
        ),
        migrations.AlterField(
            model_name='forum',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='forum_created_by', to='doma.User'),
        ),
        migrations.AlterField(
            model_name='home',
            name='village',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='doma.Village'),
        ),
    ]
