from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest

# 'DEFAULT_CONTENT_NEGOTIATION_CLASS': 'rest_framework.negotiation.DefaultContentNegotiation'

from rest_framework.negotiation import DefaultContentNegotiation
from rest_framework import parsers


# django的解析器
class DjangoView(View):

    def get(self, request):
        # request是WSGIRequest实例化的对象
        print(type(request))
        # django解析器只能解析form-data和urlencoded格式数据，不能解析json格式数据
        return HttpResponse('Django的解析器测试')


from rest_framework.views import APIView
from rest_framework.response import Response


# DRF的解析器
class DRFParserView(APIView):
    # parser_classes = [] # 配置解析器

    def get(self, request):
        # request是用rest_framework.request.Request类重新封装的request
        print(type(request))

        return Response('DRF解析器测试')



