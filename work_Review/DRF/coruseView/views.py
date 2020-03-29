from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse


class Course(APIView):
    
    def get(self, request):
        res = "handlerResponse('跨域测试')"
        return HttpResponse(res)

    def put(self, request):
        return Response('PUT')