# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-10 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artistapi', '0002_album_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='actualArtist',
            field=models.CharField(default='sting', max_length=128),
            preserve_default=False,
        ),
    ]
