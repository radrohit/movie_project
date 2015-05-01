# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_list', '0008_auto_20150429_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='genre_meta',
            field=models.TextField(max_length=100, default=''),
        ),
    ]
