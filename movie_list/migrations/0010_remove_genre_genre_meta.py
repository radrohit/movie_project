# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_list', '0009_genre_genre_meta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='genre_meta',
        ),
    ]
