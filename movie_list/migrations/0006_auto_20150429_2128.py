# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('movie_list', '0005_auto_20150429_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='mpaa_rating',
            field=models.CharField(default='N/A', max_length=5, choices=[('G', 'G'), ('PG', 'PG'), ('PG-13', 'PG-13'), ('R', 'R'), ('NC-17', 'NC-17'), ('N/A', 'Not Available')]),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.DecimalField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], decimal_places=1, max_digits=1),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(2100), django.core.validators.MinValueValidator(1880)], default=2015),
        ),
    ]
