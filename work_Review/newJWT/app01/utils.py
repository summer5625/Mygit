# -*- coding: utf-8 -*-
# @Time    : 2020/3/5  14:45
# @Author  : XiaTian
# @File    : utils.py
from app01.models import User
from django.db.models import Q
from django.contrib.auth.backends import ModelBackend


def jwt_response_payload_handler(token, user=None, request=None):
    """
    自定义jwt认证成功返回数据
    """
    return {
        'token': token,
        'id': user.id,
        'username': user.username
    }


def get_user_account_mobile(account):

    try:
        user = User.objects.filter(Q(username=account) | Q(mobile=account)).first()
    except User.DoesNotExist:
        return None
    else:
        return user


class UsernameMobileAuthBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):

        user = get_user_account_mobile(username)

        if user and user.check_password(password) and user.is_authenticated:
            return user
        else:
            return None 


























