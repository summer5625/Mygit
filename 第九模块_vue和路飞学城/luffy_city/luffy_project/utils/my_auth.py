# -*- coding: utf-8 -*-
# @Time    : 2019/11/29  15:23
# @Author  : XiaTian
# @File    : my_auth.py
import redis
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .redis_pool import POOL
from Course import models

# redis认证模块

CONN = redis.Redis(connection_pool=POOL)


class LoginAuth(BaseAuthentication):

    def authenticate(self, request):

        # 从请求头中获取登录成功后的token
        token = request.META.get('HTTP_AUTHENTICATION', '')
        if not token:
            raise AuthenticationFailed('没有携带token')

        # 去redis中比对token是否合法
        user_id = CONN.get(str(token))
        if user_id == None:
            raise AuthenticationFailed('token过期')
        user_obj = models.Account.objects.filter(id=user_id).first()

        return user_obj, token
