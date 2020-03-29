# -*- coding: utf-8 -*-
# @Time    : 2019/11/26  15:18
# @Author  : XiaTian
# @File    : serializers.py

from rest_framework import serializers
from SerDemo import models


class AuthorSerializers(serializers.Serializer):

    id = serializers.IntegerField()
    name = serializers.CharField(max_length=32)


class PublisherSerializers(serializers.Serializer):

    id = serializers.IntegerField()
    title = serializers.CharField(max_length=32)


# 自定义DRF验证的钩子函数
def my_validate(value):

    if '敏感信息' in value.lower():
        raise serializers.ValidationError('不能含有敏感信息')
    else:
        return value

# 使用Serializer序列化器进行序列化，相当于forms组件的Form
# 新建一个类继承serializers.Serializer类
# class BookSerializers(serializers.Serializer):
#
#     # required字段是用来，校验前端提交过来的数据，当为False时，不校验该字段，主要用于用户提交post请求，向数据库里面增加修改数据时，用了校验数据合法性
#     id = serializers.IntegerField(required=False)
#     title = serializers.CharField(max_length=32, validators=[my_validate]) # 使用自定义验证的钩子函数
#
#     # category字段是一个选择项，当用户提交post请求时，前端向后端提交数据时，只需要提交该字段选中的ID,不需要详细信息；但是当用户发送get
#     # 请求时又需要该字段的详细信息
#     CHOICES = ((1, 'python'), (2, 'Go'), (3, 'Linux'))
#     # read_only=True表示该字段只用来返回数据给前端，只在前端显示，只做序列化时使用
#     category = serializers.ChoiceField(choices=CHOICES, source='get_category_display', read_only=True)
#     # write_only=True只用来前端发送post请求给后端使用，只做反序列化时使用
#     w_category = serializers.ChoiceField(choices=CHOICES, write_only=True)
#     pub_time = serializers.DateField()
#
#     # 对于外键和多对多字段，同样用户提交post请求时，也只需要传给后端该选项的id
#     publisher = PublisherSerializers(read_only=True)
#     publisher_id = serializers.IntegerField(write_only=True)
#
#     author = AuthorSerializers(many=True, read_only=True) # many=True料表明表关系是多对多关系
#     author_list = serializers.ListField(write_only=True)
#
#     def create(self, validated_data):
#
#         book = models.Book.objects.create(title=validated_data['title'], category=validated_data['w_category'],
#                                    pub_time=validated_data['pub_time'], publisher_id=validated_data['publisher_id'])
#
#         book.author.add(*validated_data['author_list'])
#         return book
#
#     def update(self, instance, validated_data):
#         # 参数instance是要更新的对象， validated_data验证通过的数据
#
#         # 两个参数表示：如果验证通过的数据中有title就用验证通过的数据，如果没有就用原来的
#         instance.title = validated_data.get('title', instance.title)
#         instance.category = validated_data.get('category', instance.category)
#         instance.pub_time = validated_data.get('pub_time', instance.pub_time)
#         instance.publisher_id = validated_data.get('publisher_id', instance.publisher_id)
#
#         # 取多对多的数据
#         if validated_data.get('author_list'):
#             instance.author.set(*validated_data['author_list'])
#
#         instance.save()
#         return instance
#
#     # DRF的验证，提供了钩子函数，可以对某个字段进行校验，和modelform里面的校验钩子函数作用一样
#     def validate_title(self, value):
#
#         if "python" not in value.lower():
#             raise serializers.ValidationError('标题必须含义python')
#         return value
#
#     # 全局的DRF的验证
#     def validate(self, attrs):
#         # attrs存放所有的字段字典
#         if attrs['w_category'] == 1 and attrs['publisher_id'] == 2:
#
#             return attrs
#         else:
#             raise serializers.ValidationError('分类和出版社不符合要求')
#
#     """
#         注意：
#             自定义的DRF验证函数的优先级要高于全局的和部分校验的优先级，同时存在的话优先检验自定义的钩子函数
#     """



# 前端发送给后的数据的样板

data = {
    "title": "渗透测试",
    "w_category": 1,
    "pub_time": "2019-05-05",
    "publisher_id": 2,
    "author_list": [1, 2]
}


# 使用ModelSerializer序列化器进行序列化，和Modelform组件相同，不用自己定义字段了，直接使用数据库中表的字段
# class BookSerializers(serializers.ModelSerializer):
#
#     category = serializers.CharField(source='get_category_display')
#     publisher = serializers.SerializerMethodField()
#     author = serializers.SerializerMethodField()
#
#     # 自定义的方法名称必须是这种格式: get_字段名称()
#     def get_publisher(self, obj):
#         # obj是序列化的每一个book对象
#         publisher_obj = obj.publisher
#         return {"id": publisher_obj.id, "title": publisher_obj.title}
#
#     def get_author(self, obj):
#         authors_query_set = obj.author.all()
#         return [{"id": author_obj.id, "name": author_obj.name} for author_obj in authors_query_set]
#
#     class Meta:
#         model = models.Book
#         fields = '__all__'   # all获取所有字段    ['title', 'category']：获取部分字段
#         depth = 1  # depth = 1表示有关联着字段时，会向下找1层关联字段，如果不加depth那么关联字段只会显示关联字段的id

        # """
        #     这种获取数据库信息方法会获取所有字段的详细信息，要想只获取某个字段的部分信息需要自己定义，同时该方法对于category字段，查找时
        #     只会查找id，不能查找详细信息，也需要自己重新定义
        # """

# 使用ModelSerializer序列化器进行反序列化
class BookSerializers(serializers.ModelSerializer):

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
