# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_list', '0020_auto_20150501_1333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='rating',
            new_name='imdb_rating',
        ),
        migrations.AlterField(
            model_name='genre',
            name='genre_description',
            field=models.TextField(max_length=300, blank=True),
        ),
    ]
