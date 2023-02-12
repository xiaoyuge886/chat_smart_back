#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2023/2/12 17:46
# @Author  : gy
# @File    : smart_throttling.py
# @Software: PyCharm
from rest_framework.throttling import SimpleRateThrottle


class UserRateThrottle(SimpleRateThrottle):
    """
    Limits the rate of API calls that may be made by a given user.

    The user id will be used as a unique cache key if the user is
    authenticated.  For anonymous requests, the IP address of the request will
    be used.
    """
    scope = 'user'

    def get_cache_key(self, request, view):
        if request.user.is_authenticated:
            # 返回用户标示
            ident = request.user.pk
        else:
            # 返回`ip`标示
            ident = self.get_ident(request)

        return self.cache_format % {
            'scope': self.scope,
            'ident': ident
        }