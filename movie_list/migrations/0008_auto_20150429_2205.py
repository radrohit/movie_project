# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_list', '0007_auto_20150429_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='genre_description',
            field=models.TextField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre_id',
            field=models.ManyToManyField(to='movie_list.Genre'),
        ),
    ]
