import uuid
import redis
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from Login import serializer
from utils.BaseResponse import BaseResponse
from utils.redis_pool import POOL
from Course import models
from utils.my_auth import LoginAuth
from utils.geetest import GeetestLib


# 注册视图
class RegisterView(APIView):

    def post(self, request):
        res = BaseResponse()
        ser_obj = serializer.RegisterSerializer(data=request.data)

        if ser_obj.is_valid():
            ser_obj.save()
            res.data = ser_obj.data
        else:
            res.code = 1020
            res.error = ser_obj.errors

        return Response(res.dict)


class LoginView(APIView):

    def post(self, request):
        res = BaseResponse()
        username = request.data.get('username')
        pwd = request.data.get('pwd')

        user_obj = models.Account.objects.filter(username=username, pwd=pwd).first()

        if not user_obj:
            res.code = 1031
            res.error = '用户名或者密码错误'
        conn = redis.Redis(connection_pool=POOL)
        # 用户登录成功创建一个token，存到redis中
        try:
            token = uuid.uuid4()
            # conn.set(str(token), user_obj.id, ex=60) # ex是用来设置过期时间
            conn.set(str(token), user_obj.id) 
            res.code = 1030
            res.data = token
        except Exception as e:

            res.code = 1032
            res.error = '创建令牌失败'

        return Response(res.dict)


class TestView(APIView):

    authentication_classes = [LoginAuth] # 添加认证类

    def get(self, request):
        return Response('认证接口测试')


pc_geetest_id = "b46d1900d0a894591916ea94ea91bd2c"
pc_geetest_key = "36fc3fe98530eea08dfc6ce76e3d24c4"
REDIS_CONN = redis.Redis(connection_pool=POOL)


class GeetestView(APIView):

    def get(self, request):

        user_id = "test"
        gt = GeetestLib(pc_geetest_id, pc_geetest_key)
        status = gt.pre_process(user_id)
        REDIS_CONN.set(gt.GT_STATUS_SESSION_KEY, status)
        REDIS_CONN.set("get_user_id", user_id)
        response_str = gt.get_response_str()
        return HttpResponse(response_str)


    def post(self, request):

        gt = GeetestLib(pc_geetest_id, pc_geetest_key)
        challenge = request.POST.get(gt.FN_CHALLENGE, '')
        validate = request.POST.get(gt.FN_VALIDATE, '')
        seccode = request.POST.get(gt.FN_SECCODE, '')
        # status = request.session[gt.GT_STATUS_SESSION_KEY]
        status = REDIS_CONN.get(gt.GT_STATUS_SESSION_KEY)
        # user_id = request.session["user_id"]
        user_id = REDIS_CONN.get("get_user_id")
        # print(user_id)
        # print(status)
        if status:
            result = gt.success_validate(challenge, validate, seccode, user_id)
            # print(result)
        else:
            result = gt.failback_validate(challenge, validate, seccode)
        result = {"status": "success"} if result else {"status": "fail"}

        return HttpResponse(json.dumps(result))















