from django.db import models


# 客户表
class Customer(models.Model):

    name = models.CharField(verbose_name='姓名', max_length=32)
    age = models.CharField(verbose_name='年龄', max_length=32)
    email = models.EmailField(verbose_name='邮箱', max_length=32)
    company = models.CharField(verbose_name='公司', max_length=32)

    def __str__(self):
        return self.name


# 付费记录
class Payment(models.Model):

    customer = models.ForeignKey(verbose_name='关联客户', to='Customer', on_delete=models.CASCADE)
    money = models.IntegerField(verbose_name='付费金额')
    create_time = models.DateTimeField(verbose_name='付费时间', auto_now_add=True)