from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.core import serializers
from demon import models
import json


# ######################################################HttpResponse, JsonResponse序列化
# class BookView(View):
#
#     def get(self, request):
#
#         book_list = models.Book.objects.all().values('id', 'title', 'pub_time', 'publisher')
#         book_list = list(book_list)  # 将queryset类型转换成list类型
#         # ret = json.dumps(book_list, ensure_ascii=False)
#
#         # 获取外键字段内容需要循环获取外键 再去数据库查然后拼接成我们想要的
#         ret = []
#
#         for book in book_list:
#             publisher_id = book['publisher']
#             publisher_obj = models.Publisher.objects.filter(id=publisher_id).first()
#             book['publisher'] = {
#                 'id': publisher_id,
#                 'title': publisher_obj.title
#             }
#             ret.append(book)
#
#         # return HttpResponse(ret) # HttpResponse不能序列化时间
#         return JsonResponse(ret, safe=False, json_dumps_params={'ensure_ascii': False})


# ######################################################HttpResponse, JsonResponse序列化
from rest_framework.views import APIView  # 视图类要继承的类
from rest_framework.response import Response  #  返回值的序列化器
from demon.serializers import BookSerializer


class GenericViews(APIView):

    query_set = None
    serializer_class = None

    def get_queryset(self):
        return self.query_set

    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)


class ViewHandlerMixin(object):

    def list(self, request):
        query = self.get_queryset()
        ret = self.get_serializer(query, many=True)
        return Response(ret.data)


class CreateHandlerMixin(object):

    def create(self, request):

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.validate)
        else:
            return Response(serializer.errors)


class RetrieveModelMixin(object):

    def retrieve(self, request, id):

        book = self.get_queryset().filter(id=id).first()
        ret = BookSerializer(book)
        return Response(ret.data)


class EditModelMixin(object):

    def update(self, request, id):

        book_obj = self.get_queryset().filter(id=id).first()
        serializer = self.get_serializer(book_obj, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data)
        else:
            return Response(serializer.errors)


class DelModelMixin(object):

    def distroy(self, request, id):

        book_obj = self.get_queryset().filter(id=id).first()
        book_obj.delete()
        return Response("")


class ListView(GenericViews, ViewHandlerMixin, CreateHandlerMixin):
    pass


class EditView(GenericViews, RetrieveModelMixin, EditModelMixin, DelModelMixin):
    pass


class BookView(ListView):

    query_set = models.Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request):

        return self.list(request)

    def post(self, request):
        
        return self.create(request)


class BookEditView(EditView):

    query_set = models.Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, id):
        return self.retrieve(request, id)
        
    def put(self, request, id):

       return self.update(request, id)

    def delete(self, request, id):

        return self.distroy(request, id)


from rest_framework.viewsets import ViewSetMixin



class BookSerializers(ViewSetMixin, GenericViews, ViewHandlerMixin, CreateHandlerMixin, RetrieveModelMixin, EditModelMixin, DelModelMixin):
    pass


class BookModelViewSet(BookSerializers):

    query_set = models.Book.objects.all()
    serializer_class =BookSerializer































































