# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kind', models.IntegerField(verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(1, b'App Key'), (2, b'App Secret'), (3, b'Access Token'), (4, b'Callback Url')])),
                ('value', models.CharField(max_length=200, verbose_name=b'\xe5\x80\xbc')),
            ],
            options={
                'verbose_name_plural': '\u914d\u7f6e',
            },
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.IntegerField(verbose_name=b'uid')),
                ('screen_name', models.CharField(max_length=100, verbose_name=b'\xe6\x98\xb5\xe7\xa7\xb0')),
                ('avatar', models.CharField(default=b'', max_length=500, verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f')),
                ('description', models.CharField(default=b'', max_length=500, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe4\xb8\xaa\xe4\xba\xba\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('followers_count', models.IntegerField(default=0, verbose_name=b'\xe7\xb2\x89\xe4\xb8\x9d\xe6\x95\xb0')),
                ('friends_count', models.IntegerField(default=0, verbose_name=b'\xe5\x85\xb3\xe6\xb3\xa8\xe6\x95\xb0')),
                ('statuses_count', models.IntegerField(default=0, verbose_name=b'\xe5\xbe\xae\xe5\x8d\x9a\xe6\x95\xb0')),
                ('favourites_count', models.IntegerField(default=0, verbose_name=b'\xe6\x94\xb6\xe8\x97\x8f\xe6\x95\xb0')),
            ],
            options={
                'verbose_name_plural': '\u597d\u53cb',
            },
        ),
        migrations.CreateModel(
            name='Weibo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.IntegerField(verbose_name=b'uid')),
                ('weibo_id', models.IntegerField(verbose_name=b'\xe5\xbe\xae\xe5\x8d\x9aid')),
                ('mid', models.IntegerField(verbose_name=b'mid')),
                ('text', models.TextField(verbose_name=b'\xe5\xbe\xae\xe5\x8d\x9a\xe4\xbf\xa1\xe6\x81\xaf\xe5\x86\x85\xe5\xae\xb9')),
                ('user', models.TextField(default=b'', verbose_name=b'\xe5\xbe\xae\xe5\x8d\x9a\xe4\xbd\x9c\xe8\x80\x85\xe7\x9a\x84\xe7\x94\xa8\xe6\x88\xb7\xe4\xbf\xa1\xe6\x81\xaf\xe5\xad\x97\xe6\xae\xb5')),
                ('reposts_count', models.IntegerField(default=0, verbose_name=b'\xe8\xbd\xac\xe5\x8f\x91\xe6\x95\xb0')),
                ('comments_count', models.IntegerField(default=0, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe6\x95\xb0')),
                ('attitudes_count', models.IntegerField(default=0, verbose_name=b'\xe8\xa1\xa8\xe6\x80\x81\xe6\x95\xb0')),
                ('created_at', models.CharField(max_length=100, verbose_name=b'\xe6\x98\xb5\xe7\xa7\xb0')),
            ],
            options={
                'verbose_name_plural': '\u5fae\u535a',
            },
        ),
    ]
