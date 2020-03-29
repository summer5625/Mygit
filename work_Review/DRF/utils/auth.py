# -*- coding: utf-8 -*-
# @Time    : 2020/2/23  22:08
# @Author  : XiaTian
# @File    : auth.py
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import BaseAuthentication
from authView import models


class MyAuth(BaseAuthentication):

    def authenticate(self, request):

        token = request.query_params.get('token')

        if not token:
            raise AuthenticationFailed('没有token')
        user_obj = models.User.objects.filter(token=token).first()
        if not user_obj:
            raise AuthenticationFailed('token不合法')

        return (user_obj, token)
