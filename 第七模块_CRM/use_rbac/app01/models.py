from django.db import models
from rbac.models import UserInfo as RbacUserInfo


# 部门表
class Department(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='部门', max_length=32)

    def __str__(self):

        return self.title


# 用户表
class Userinfo(RbacUserInfo):

    phone = models.CharField(verbose_name='联系方式', max_length=32)
    level_choices = [(1, 'T1'),(2, 'T2'), (3, 'T3')]
    level = models.IntegerField(verbose_name='级别', choices=level_choices)
    depart = models.ForeignKey(verbose_name='部门', to='Department', on_delete=models.CASCADE)

    def __str__(self):

        return self.name


# 主机表
class Host(models.Model):

    id = models.AutoField(primary_key=True)
    hostname = models.CharField(verbose_name='主机名', max_length=32)
    ip = models.GenericIPAddressField(verbose_name='IP', protocol='both') # protocol='both'是 协议，支持ipv4和ipv6
    depart = models.ForeignKey(verbose_name='归属部门', to='Department', on_delete=models.CASCADE)

    def __str__(self):

        return self.hostname



