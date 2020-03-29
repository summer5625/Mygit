from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from rest_framework.views import APIView
from rest_framework.response import Response


class ParserTest(APIView):
    
    def get(self, request):
        
        print(request)
        
        return Response('解析器测试')
