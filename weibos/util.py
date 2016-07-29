# -*- coding: utf-8 -*-
__author__ = 'yijingping'

import weibo
from .models import Config


def get_weibo_client():
    app_key = Config.objects.get(kind=Config.KIND_APP_KEY).value
    app_secret = Config.objects.get(kind=Config.KIND_APP_SECRET).value
    call_back = Config.objects.get(kind=Config.KIND_CALLBACK).value
    client = weibo.APIClient(app_key, app_secret, call_back)
    return client


def get_authed_weibo_client():
    client = get_weibo_client()
    access_token = Config.objects.get(kind=Config.KIND_ACCESS_TOKEN).value
    expires_in = 0
    client.set_access_token(access_token, expires_in)
    return client

