# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-05 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='post_image',
            field=models.ImageField(null=True, upload_to='my-photos/'),
        ),
    ]