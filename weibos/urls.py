# -*- coding: utf-8 -*-
__author__ = 'yijingping'
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="weibos.index"),
    url(r'^auth/$', views.auth, name="weibos.auth"),
    url(r'^auth_callback/$', views.auth_callback, name="weibos.auth_callback"),

    url(r'^weibo/$', views.weibo_list, name="weibos.weibo_list"),
]
