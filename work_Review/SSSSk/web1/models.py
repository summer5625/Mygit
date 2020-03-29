from django.db import models


# 部门表
class Department(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='部门', max_length=32)

    def __str__(self):
        return self.title


# 用户表
class UserInfo(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='用户名', max_length=32)
    gender_choices = ((1, '男'), (2, '女'))
    gender = models.IntegerField(verbose_name='性别', choices=gender_choices, default=1)
    password = models.CharField(verbose_name='密码', max_length=64)
    email = models.CharField(verbose_name='邮箱', max_length=32)
    depart = models.ForeignKey(verbose_name='部门', to='Department', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# 主机表
class Host(models.Model):

    id = models.AutoField(primary_key=True)
    hostname = models.CharField(verbose_name='主机名', max_length=64)
    ip = models.CharField(verbose_name='IP', max_length=128)

    def __str__(self):
        return self.hostname


class Role(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='角色名称', max_length=32)

    def __str__(self):
        return self.title































