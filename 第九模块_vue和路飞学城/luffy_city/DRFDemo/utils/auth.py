# -*- coding: utf-8 -*-
# @Time    : 2019/11/27  0:30
# @Author  : XiaTian
# @File    : auth.py
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import BaseAuthentication
from authDemo import models


class MyAuth(BaseAuthentication):

    def authenticate(self, request):
        # 做认证看用户是否登录
        # 示例中将token放在url中，从url中拿到token值，然后去数据库查找对应用户的token是否存在，合法则可以获取用户信息
        token = request.query_params.get('token')
      
        if not token:
            # 没有token抛出异常
            raise AuthenticationFailed('没有携带token')
        user_obj = models.User.objects.filter(token=token).first()
        if not user_obj:
            raise AuthenticationFailed('token不合法')
        return (user_obj, token)