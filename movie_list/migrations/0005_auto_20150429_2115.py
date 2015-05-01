# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('movie_list', '0004_auto_20150429_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(2100), django.core.validators.MinValueValidator(1880)], max_length=4, default=2015),
        ),
    ]
