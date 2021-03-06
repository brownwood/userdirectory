# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 16:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='user',
            name='email_address',
            field=models.EmailField(max_length=254, verbose_name='Email Address:'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100, verbose_name='Name:'),
        ),
    ]
