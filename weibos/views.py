# -*- coding: utf-8 -*-
__author__ = 'yijingping'

from weibospider.util import login_required
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .util import get_weibo_client
from .models import Config, Friend, Weibo

import logging
logging.basicConfig()

@login_required
def index(request):
    context = {}
    return render_to_response('weibos/index.html', RequestContext(request, context))


def auth(request):
    context = {}
    client = get_weibo_client()
    auth_url = client.get_authorize_url()
    # 跳转到用户进行授权的url，将该url拷贝到浏览器中，服务器将会返回一个url，该url中包含一个code字段（如图1所示）
    print "auth_url : " + auth_url
    return redirect(auth_url)


def auth_callback(request):
    code = request.GET.get('code')
    if not code:
        messages.success(request, '认证失败.')
        return redirect('weibos.index')

    print code
    # 根据code请求access token
    client = get_weibo_client()
    rsp = client.request_access_token(code)
    client.set_access_token(rsp.access_token, rsp.expires_in)
    # 存储新的access token
    Config.objects.filter(kind=Config.KIND_ACCESS_TOKEN).update(value=rsp.access_token)
    messages.success(request, '认证成功.')
    return redirect('weibos.index')




@login_required
def weibo_list(request):
    context = {}
    # 文章信息
    params = request.GET.copy()
    _obj_list = Weibo.objects.order_by('-id')

    paginator = Paginator(_obj_list, 50 )  # Show 10 contacts per page

    page = request.GET.get('page')
    try:
        _objs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        _objs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        _objs = paginator.page(paginator.num_pages)

    context.update({
        "active_nav": "weibos.weibo",
        "weibos": _objs,
        "params": params
    })
    return render_to_response('weibos/weibo_list.html', {}, context_instance=RequestContext(request, context))

