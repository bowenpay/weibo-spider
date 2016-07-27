# -*- coding: utf-8 -*-
__author__ = 'yijingping'
from django.conf import settings
from django.shortcuts import redirect

def login_required(f):
    """
    要求登录的decorator
    :param f: 函数
    :return:
    """
    def _wrapper(request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated():
            return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        else:
            #request_context = RequestContext(request)
            #request_context.push({"admin_user": user})
            return f(request, *args, **kwargs)
    return _wrapper