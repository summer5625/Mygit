import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers # 导入serializers序列化
from django.views import View  # 导入视图样式的类，后面的视图函数就可以继承该类，该类可以响应http协议的各种请求


from SerDemo import models

# 导入rest_framwork
from rest_framework.views import APIView # 导入视图函数要继承的api类
from rest_framework.response import Response # 返回函数
from rest_framework.viewsets import ViewSetMixin # 导入ViewSetMixin，重新分配ar_view函数的匹配关系
from SerDemo.serializers import BookSerializers # 导入定义的序列化对象


# class BookView(View):

    # 用JsonResponse序列化
    # def get(self, request):
    #
    #     book_list = models.Book.objects.values('id', 'title', 'pub_time', 'publisher')
    #     book_list = list(book_list)
    #     # print(book_list)
    #     ret = []
    #     for book in book_list:
    #         publisher_id = book['publisher']
    #         # author_id = book['author']
    #         publisher_obj = models.Publisher.objects.filter(id=publisher_id).first()
    #         # author_obj = models.Author.objects.filter(id=author_id).first()
    #         book['publisher'] = {
    #             'id': publisher_id,
    #             'title': publisher_obj.title
    #         }
    #         ret.append(book)
    #
    #     # ret = json.dumps(book_list, ensure_ascii=False) # ensure_ascii=False放置在序列化时乱码,不能序列化时间对象
    #
    #     return JsonResponse(ret, safe=False, json_dumps_params={'ensure_ascii': False})

    # 用serializers序列化,关联字段时只能取到关联字段的id，不能显示详细信息，需要自己处理
    # def get(self, request):
    #
    #     book_list = models.Book.objects.all()
    #     ret = serializers.serialize('json', book_list, ensure_ascii=False)
    #
    #     print(ret)
    #     return HttpResponse(ret)


class GenericViews(APIView):

    query_set = None
    serializers_class = None

    def get_query_set(self):
        return self.query_set

    def get_serializers(self, *args, **kwargs):
        return self.serializers_class(*args, **kwargs)


class ViewHandlerMixin(object):

    def list(self, request):
        query = self.get_query_set()
        ret = self.get_serializers(query, many=True)

        return Response(ret.data)

    def create(self, request):
        serializer = self.get_serializers(data=request.data)

        if serializer.is_valid():
            # 保存数据到数据库
            serializer.save()

            # 遵循restful风格，添加数据后要返回新增数据给前端，验证通过数据在serializer.validated_data里面
            return Response(serializer.data)

        else:

            return Response(serializer.errors) # 验证不通过返回错误信


class EditViewMixin(object):

    def retrieve(self, request, id):
        obj = self.get_query_set().filter(id=id).first()
        ret = self.get_serializers(obj)
        return Response(ret.data)

    def update(self, request, id):
        obj = self.get_query_set().filter(id=id).first()
        serializer = self.get_serializers(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def destroy(self, request, id):
        obj = self.get_query_set().filter(id=id).first()
        obj.delete()
        return Response("")


# 继承APIView类
class BookView(GenericViews, ViewHandlerMixin):
    query_set = models.Book.objects.all()
    serializers_class = BookSerializers

    def get(self, request):

        # book_obj = models.Book.objects.all().first()
        # ret = BookSerializers(book_obj)

        # book_list = models.Book.objects.all()
        # ret = BookSerializers(book_list, many=True) # 序列化多个数据时要加many=True

        return self.list(request)

    def post(self, request):

        # 前端传过来的数据在request.data里面

        # serializer = BookSerializers(data=request.data)

        # 校验用户提交过来的数据是否全部通过
        # if serializer.is_valid():
        #     # 保存数据到数据库
        #     serializer.save()
        #
        #     # 遵循restful风格，添加数据后要返回新增数据给前端，验证通过数据在serializer.validated_data里面
        #     return Response(serializer.data)
        #
        # else:
        #
        #     return Response(serializer.errors) # 验证不通过返回错误信
        return self.create(request)


class BookEditView(GenericViews, EditViewMixin):
    query_set = models.Book.objects.all()
    serializers_class = BookSerializers

    def get(self, request, id):

        # book_obj = models.Book.objects.filter(id=id).first()
        # ret  = BookSerializers(book_obj)
        #
        # return Response(ret.data)
        return self.retrieve(request, id)

    def put(self, request, id):
        
        # book_obj = models.Book.objects.filter(id=id).first()
        # # 三个参数，第一个是要更新的对象，第二个是更新的数据，第三个是表示允许部分更新
        # serializer = BookSerializers(book_obj, data=request.data, partial=True)
        # if serializer.is_valid():
        #     serializer.save()
        #
        #     return Response(serializer.data)
        # else:
        #     return Response(serializer.errors)
        return self.update(request, id)

    def delete(self, request, id):
        # book_obj = models.Book.objects.filter(id=id).first()
        # book_obj.delete()
        # return Response("")

        return self.destroy(request, id)


# class ViewSetMixin(object):
#
#     def as_view(self):
#         """
#         按照指定的参数对应关系去匹配
#         get-->list  post--->create  get-->retrieve  put-->update  delete-->destroy
#         :return:
#         """
#
#         return

from rest_framework.viewsets import ModelViewSet, ViewSetMixin # 导入框架提供的ModelViewSet，

# 不继承ModelViewSet的写法
# class BookModelViewSet(ViewSetMixin, GenericViews, ViewHandlerMixin, EditViewMixin):
#     query_set = models.Book.objects.all()
#     serializers_class = BookSerializers


class BookModelViewSet(ModelViewSet):
    queryset = models.Book.objects.all() # 名字必须为queryset
    serializer_class = BookSerializers
    

"""
rest_framwork框架所有的视图类在一下四个文件中

    from rest_framework import views
    from rest_framework import generics  # 包含了公共的视图类
    from rest_framework import mixins  # 混合继承的类
    from rest_framework import viewsets

"""












