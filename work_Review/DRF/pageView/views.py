from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import pagination
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from demon.serializers import BookSerializer
from utils.paginater import MyPagination
from demon import models


class Book(GenericAPIView, ListModelMixin):

    queryset = models.Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = MyPagination

    def get(self, request):

        return self.list(request)


