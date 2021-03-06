# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-21 13:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20181021_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='neighborhood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alerts', to='app.Neighborhood'),
        ),
        migrations.AlterField(
            model_name='business',
            name='neighborhood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='businesses', to='app.Neighborhood'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='neighborhood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='members', to='app.Neighborhood'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='profpics/prof.png', upload_to='profpics/'),
        ),
    ]
