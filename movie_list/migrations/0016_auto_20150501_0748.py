# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_list', '0015_auto_20150501_0727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_poster',
            field=models.ImageField(upload_to='poster'),
        ),
    ]
