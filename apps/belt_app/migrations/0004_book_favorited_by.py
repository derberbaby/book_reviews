# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-27 00:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt_app', '0003_user_friend'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='favorited_by',
            field=models.ManyToManyField(related_name='favorite_books', to='belt_app.User'),
        ),
    ]