# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weibos', '0002_auto_20160727_1149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kind', models.IntegerField(default=1, verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(0, b'\xe5\x85\xb3\xe9\x94\xae\xe8\xaf\x8d'), (1, b'\xe8\xaf\x9d\xe9\xa2\x98')])),
                ('text', models.CharField(max_length=100, verbose_name=b'\xe8\xaf\x8d')),
            ],
            options={
                'verbose_name_plural': '\u8bcd',
            },
        ),
        migrations.AlterField(
            model_name='weibo',
            name='created_at',
            field=models.CharField(max_length=100, verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
