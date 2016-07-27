# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weibos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='uid',
            field=models.BigIntegerField(verbose_name=b'uid'),
        ),
        migrations.AlterField(
            model_name='weibo',
            name='mid',
            field=models.BigIntegerField(verbose_name=b'mid'),
        ),
        migrations.AlterField(
            model_name='weibo',
            name='uid',
            field=models.BigIntegerField(verbose_name=b'uid'),
        ),
        migrations.AlterField(
            model_name='weibo',
            name='weibo_id',
            field=models.BigIntegerField(verbose_name=b'\xe5\xbe\xae\xe5\x8d\x9aid'),
        ),
    ]
