# -*- coding: utf-8 -*-
# @Time    : 2019/11/28  15:49
# @Author  : XiaTian
# @File    : serializer.py
import hashlib
from rest_framework import serializers
from Course import models


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = '__all__'

    def create(self, validated_data):

        pwd = validated_data['pwd']
        pwd_salt = 'luffy_password' + pwd
        md5_str = hashlib.md5(pwd_salt.encode()).hexdigest()

        user_obj = models.Account.objects.create(username=validated_data['username'], pwd=md5_str)

        return user_obj
















