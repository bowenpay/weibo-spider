# -*- coding: utf-8 -*-
from __future__ import unicode_literals
__author__ = 'yijingping'
# 加载django环境
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
os.environ['DJANGO_SETTINGS_MODULE'] = 'weibospider.settings'
import django
django.setup()

import weibo
import argparse
from weibos.util import get_authed_weibo_client
from weibos.models import Weibo

import json
import logging
logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class WeiboScript(object):
    """ 统计干部注册数
    """
    def __init__(self):
        self.client = get_authed_weibo_client()

    def run(self):
        pass

    def timeline(self):
        """ 同步时间线 """
        for page in range(10):
            data = self.client.statuses.home_timeline.get(page=page+1)
            statuses = data['statuses']
            for item in statuses:
                user = item["user"]
                Weibo.objects.update_or_create(weibo_id=item['id'], defaults={
                    "uid": user["id"],
                    "weibo_id": item["id"],
                    "mid": item["mid"],
                    "text": item["text"],
                    "user": json.dumps(user),
                    "reposts_count": item["reposts_count"],
                    "comments_count": item["comments_count"],
                    "attitudes_count": item["attitudes_count"],
                    "created_at": item["created_at"],
                })


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--timeline", action="store_true", help="获取最新微博")
    args = parser.parse_args()
    if args.timeline:
        statsUser = WeiboScript()
        statsUser.timeline()
    else:
        print 'usage: python weibo_script.py --help'