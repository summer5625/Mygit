from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class DemoView(APIView):

    def get(self, request):

        print(request.version)
        print(request.versioning_scheme)

        if request.version == 'v1':
            return Response('V1版本的数据')
        elif request.version == 'v2':
            return Response('v2版本的数据')

        return Response('版本不存在')