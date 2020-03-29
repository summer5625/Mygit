from rest_framework.views import APIView
from rest_framework.response import Response
import uuid
from authDemo import models
from utils.auth import MyAuth
from utils.permission import MyPermission
from utils.throttle import MyThrottle


class AuthView(APIView):

    def get(self, request):

        return Response('认证的Demo')


class LoginView(APIView):

    def post(self, request):

        username = request.data.get('username')
        pwd = request.data.get('password')
        # 登录成功生成token
        token = uuid.uuid4()
        models.User.objects.create(username=username, password=pwd, token=token)
        return Response('创建用户成功')


class TestView(APIView):
    authentication_classes = [MyAuth, ]  # 配置局部视图的认证
    permission_classes = [MyPermission, ] # 配置权限类
    throttle_classes = [MyThrottle, ]  # 配置频率限制类

    def get(self, request):

        # print(request.user)
        # print(request.auth)
        return Response('认证测试')