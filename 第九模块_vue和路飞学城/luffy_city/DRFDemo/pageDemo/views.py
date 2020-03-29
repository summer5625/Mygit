from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import pagination
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from utils.paginater import MyPagination
from SerDemo import models
from SerDemo.serializers import BookSerializers


# Create your views here.


# 自己定义的方法
# class BookView(APIView):
#
#     def get(self, request):
#         queryset = models.Book.objects.all()
#
#         # 1、实例化分页器对象
#         page_obj = MyPagination()
#         # 2、调用分页方法去分页queryset
#         page_queryset = page_obj.paginate_queryset(queryset, request, view=self)
#         # 3、把分页好的数据序列化返回
#
#         # 4、带着上一页，下一页的连接
#
#         ser_obj = BookSerializers(page_queryset, many=True)
#
#         return page_obj.get_paginated_response(ser_obj.data)


# 使用组件提供的方法
class BookView(GenericAPIView, ListModelMixin):
    queryset = models.Book.objects.all()
    serializer_class = BookSerializers
    pagination_class = MyPagination
    # 找self.paginate_queryset(queryset)方法

    def get(self, request):

        return self.list(request)

