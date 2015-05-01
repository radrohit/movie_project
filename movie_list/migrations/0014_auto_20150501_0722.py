# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_list', '0013_auto_20150430_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_poster',
            field=models.ImageField(upload_to='poster', default='C:\\Users\\Rohith\\Desktop\\movie_project\\static\\images\\poster/default.jpg'),
        ),
    ]
