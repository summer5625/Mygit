from django.db import models


# Create your models here.


class Menu(models.Model):
    mid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='一级菜单名称', max_length=32)
    icon = models.CharField(verbose_name='图标', max_length=64)

    def __str__(self):
        return self.title


class Permission(models.Model):
    """
    权限表
    """
    pid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='标题', max_length=32)
    url = models.CharField(verbose_name='含正则的URL', max_length=128)
    name = models.CharField(verbose_name='URL的别名', max_length=32, unique=True, null=True, blank=True)  # 设置权限粒度用

    menu = models.ForeignKey(verbose_name='所属菜单', to='Menu', null=True, blank=True, help_text='null表示不是菜单;非null表示二级菜单',
                             on_delete=models.CASCADE)
    p_id = models.ForeignKey(verbose_name='关联的权限', to='Permission', null=True, blank=True, related_name='parents',
                             help_text='对于费菜单权限需要选择一个菜单权限，用户点击非菜单权限时，关联的菜单权限默认展开', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# 角色表
class Role(models.Model):
    rid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='角色名称', max_length=32)
    permissions = models.ManyToManyField(verbose_name='拥有的所有权限', to='Permission', blank=True)

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    """
    用户表
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)
    email = models.CharField(verbose_name='邮箱', max_length=32)
    roles = models.ManyToManyField(verbose_name='拥有的所有角色', to='Role', blank=True)

    def __str__(self):
        return self.name


