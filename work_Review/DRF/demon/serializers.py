# -*- coding: utf-8 -*-
# @Time    : 2020/2/21  17:19
# @Author  : XiaTian
# @File    : serializers.py
from rest_framework import serializers
from demon import models


# class PublisherSerializer(serializers.Serializer):
#
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=32)
#
#
# class AuthorSerializer(serializers.Serializer):
#
#     id = serializers.IntegerField()
#     name = serializers.CharField(max_length=32)


# 自定义DRF验证的钩子函数
# def my_validate(value):
#
#     if '敏感信息' in value.lower():
#         raise serializers.ValidationError('不能含有敏感信息')
#     else:
#         return value
    
    
# class BookSerializer(serializers.Serializer):
#
#     id = serializers.IntegerField(required=False)
#     title = serializers.CharField(max_length=32, validators=[my_validate])
#     CHOICES = ((1, "Linux"), (2, "Django"), (3, "Python"))
#
#     # 对于可选择的字段，要显示选中的信息，就需要source参数，值和ORM中获取选择字段的方法一样
#     category = serializers.ChoiceField(choices=CHOICES, source="get_category_display", read_only=True)
#     c_category = serializers.ChoiceField(choices=CHOICES, write_only=True)
#     pub_time = serializers.DateField()
#     publisher = PublisherSerializer(read_only=True)
#     publisher_id = serializers.IntegerField(write_only=True)
#
#     author = AuthorSerializer(many=True, read_only=True)  # many=True代表关联表是多对多的关系
#     author_list = serializers.ListField(write_only=True)
#
#     def create(self, validated_data):
#
#         book = models.Book.objects.create(title=validated_data['title'], category=validated_data['c_category'],
#                                           publisher_id=validated_data['publisher_id'], pub_time=validated_data['pub_time'])
#         book.author.add(*validated_data['author_list'])
#
#         return book
#
#     def update(self, instance, validated_data):
#
#         instance.title = validated_data.get('title', instance.title)
#         instance.category = validated_data.get('category', instance.category)
#         instance.pub_time = validated_data.get('pub_time', instance.pub_time)
#         instance.publisher_id = validated_data.get('publisher_id', instance.publisher_id)
#
#         if validated_data.get('author_list'):
#             instance.author.set(*validated_data['author_list'])
#         instance.save()
#
#         return instance
#
#     def validate_title(self, value):
#
#
#         if 'python' not in value.lower():
#             raise serializers.ValidationError('标题必须含有python')
#
#         return value
#
#     def validate(self, attrs):
#         print(attrs)
#         # attrs存放所有的字段字典
#         if attrs['c_category'] == 1 and attrs['publisher_id'] == 2:
#
#             return attrs
#         else:
#             raise serializers.ValidationError('分类和出版社不符合要求')
        

# ###############################################ModelSerializer序列化
# 使用ModelSerializer序列化器进行反序列化
class BookSerializer(serializers.ModelSerializer):

    category_display = serializers.SerializerMethodField(read_only=True)
    publisher_info = serializers.SerializerMethodField(read_only=True)
    authors_info = serializers.SerializerMethodField(read_only=True)

    def get_category_display(self, obj):
        return obj.get_category_display()

    # 自定义的方法名称必须是这种格式: get_字段名称()
    def get_publisher_info(self, obj):
        # obj是序列化的每一个book对象
        publisher_obj = obj.publisher
        return {"id": publisher_obj.id, "title": publisher_obj.title}

    def get_authors_info(self, obj):
        authors_query_set = obj.author.all()
        return [{"id": author_obj.id, "name": author_obj.name} for author_obj in authors_query_set]

    class Meta:
        model = models.Book
        fields = '__all__'   # all获取所有字段    ['title', 'category']：获取部分字段

        extra_kwargs = {
            "category": {'write_only': True},
            "publisher": {'write_only': True},
            "author": {'write_only': True},
        } # 表明该字段在反序列化时使用

        """
            添加数据时不用再定义create方法了
        """



































