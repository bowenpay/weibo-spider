# -*- coding: utf-8 -*-
__author__ = 'yijingping'

import json
from django.db import models


class Config(models.Model):
    KIND_APP_KEY = 1
    KIND_APP_SECRET = 2
    KIND_ACCESS_TOKEN = 3
    KIND_CALLBACK = 4
    KIND_CHOICES = (
        (KIND_APP_KEY, 'App Key'),
        (KIND_APP_SECRET, 'App Secret'),
        (KIND_ACCESS_TOKEN, 'Access Token'),
        (KIND_CALLBACK, 'Callback Url'),
    )
    kind = models.IntegerField(choices=KIND_CHOICES, verbose_name="类型")
    value = models.CharField(max_length=200, verbose_name="值")

    def __unicode__(self):
        return '%s' % self.kind

    class Meta:
        verbose_name_plural = "配置"


class Friend(models.Model):
    uid = models.BigIntegerField(verbose_name="uid")
    screen_name = models.CharField(max_length=100, verbose_name="昵称")
    avatar = models.CharField(max_length=500, default='', verbose_name='头像')
    description = models.CharField(max_length=500, default='', verbose_name='用户个人描述')
    followers_count = models.IntegerField(default=0, verbose_name="粉丝数")
    friends_count = models.IntegerField(default=0, verbose_name="关注数")
    statuses_count = models.IntegerField(default=0, verbose_name="微博数")
    favourites_count = models.IntegerField(default=0, verbose_name="收藏数")

    def __unicode__(self):
        return self.screen_name

    class Meta:
        verbose_name_plural = "好友"


class Weibo(models.Model):
    uid = models.BigIntegerField(verbose_name="uid")
    weibo_id = models.BigIntegerField(verbose_name="微博id")
    mid = models.BigIntegerField(verbose_name="mid")
    text = models.TextField(verbose_name="微博信息内容")
    user = models.TextField(default='', verbose_name="微博作者的用户信息字段")
    reposts_count = models.IntegerField(default=0, verbose_name="转发数")
    comments_count = models.IntegerField(default=0, verbose_name="评论数")
    attitudes_count = models.IntegerField(default=0, verbose_name="表态数")
    created_at = models.CharField(max_length=100, verbose_name="发布时间")

    def __unicode__(self):
        return self.text

    def get_user(self):
        user = json.loads(self.user)
        return user

    class Meta:
        verbose_name_plural = "微博"


