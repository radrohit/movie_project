# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_list', '0002_auto_20150429_2019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='description',
            new_name='movie_description',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='name',
            new_name='movie_name',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='poster',
            new_name='movie_poster',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
        migrations.AddField(
            model_name='movie',
            name='mpaa_rating',
            field=models.CharField(default='N/A', choices=[('G', 'General Audience'), ('PG', 'Parental Guidance'), ('PG-13', 'Parents Cautioned'), ('R', 'Restricted'), ('NC-17', 'Above 17'), ('N/A', 'Not Available')], max_length=5),
        ),
    ]
