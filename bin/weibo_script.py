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
from weibos.models import Weibo, Word

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

    def save_weibo(self, status):
        user = status["user"]
        Weibo.objects.update_or_create(weibo_id=status['id'], defaults={
                    "uid": user["id"],
                    "weibo_id": status["id"],
                    "mid": status["mid"],
                    "text": status["text"],
                    "user": json.dumps(user),
                    "reposts_count": status["reposts_count"],
                    "comments_count": status["comments_count"],
                    "attitudes_count": status["attitudes_count"],
                    "created_at": status["created_at"],
                })

    def save_statuses(self, statuses):
        for item in statuses:
            self.save_weibo(item)

    def timeline(self):
        """ 同步时间线 """
        for page in range(1):
            data = self.client.statuses.home_timeline.get(page=page+1, count=100)
            statuses = data['statuses']
            self.save_statuses(reversed(statuses))

    def search_topics(self):
        """ 话题搜索 """
        topics = Word.objects.filter(kind=Word.KIND_TOPIC).values_list('text', flat=True)
        for q in topics:
            for page in range(1):
                data = self.client.search.topics.get(q=q, page=page+1, count=50)
                statuses = data['statuses']
                self.save_statuses(reversed(statuses))

    def search_keywords(self):
        """ 话题搜索 """
        topics = Word.objects.filter(kind=Word.KIND_KEYWORD).values_list('text', flat=True)
        for q in topics:
            for page in range(1):
                data = self.client.search.statuses.get(q=q, page=page+1, count=50)
                statuses = data['statuses']
                self.save_statuses(reversed(statuses))

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--timeline", action="store_true", help="获取最新微博")
    parser.add_argument("--search_topics", action="store_true", help="搜索某一话题下的微博")
    parser.add_argument("--search_keywords", action="store_true", help="搜索含某关键词的微博")
    args = parser.parse_args()
    if args.timeline:
        statsUser = WeiboScript()
        statsUser.timeline()
    elif args.search_topics:
        statsUser = WeiboScript()
        statsUser.search_topics()
    elif args.search_keywords:
        statsUser = WeiboScript()
        statsUser.search_keywords()
    else:
        print 'usage: python weibo_script.py --help'