from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse


class CorsView(APIView):
    
    def get(self, request):

        ret = "handlerResponse('跨域测试')"
        
        return HttpResponse(ret)

    def put(self, request):

        return Response('put接口测试')

    def post(self, request):

        return Response('post测试')


