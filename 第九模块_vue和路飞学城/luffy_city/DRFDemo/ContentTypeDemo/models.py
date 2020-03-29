from django.db import models
from django.contrib.contenttypes.models import ContentType  # 导入ContentType表格
from django.contrib.contenttypes.fields import GenericForeignKey # GenericForeignKey用于进行查询，主要关联表名和表中的数据
from django.contrib.contenttypes.fields import GenericRelation


class Food(models.Model):

    title = models.CharField(verbose_name='食物名称', max_length=32)

    # 不会生成字段，只用于反向查询
    coupons = GenericRelation(to='Coupon')
    
    def __str__(self):
        return self.title


class Fruit(models.Model):

    title = models.CharField(verbose_name='水果名称', max_length=32)

    # 不会生成字段，只用于反向查询
    coupons = GenericRelation(to='Coupon')
    
    def __str__(self):
        return self.title


class Coupon(models.Model):
    """
        id     title     table_id      object_id
        1     面包九五折     1               1
        2    香蕉满十减三    2               1

    """

    title = models.CharField(verbose_name='优惠券名称', max_length=64)
    # 使用django提供的contentType组件，三部曲

    # 1、第一步：创建关联的表名字段
    content_type = models.ForeignKey(to=ContentType, on_delete=None) # 与导入的表关联
    # 2、第二部：创建对应表中的对应数据字段
    object_id = models.IntegerField() # 对应关联表中的数据
    # 3、将对应的表合表中的数据关联起来，不会生成字段，只用于增删改查
    content_obj = GenericForeignKey('content_type', 'object_id') # 将对应表中对应的数据关联起来
    
    def __str__(self):
        return self.title



