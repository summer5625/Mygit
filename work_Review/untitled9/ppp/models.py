from django.db import models


# 菜单表
class Menu(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='一级菜单名', max_length=32)
    icon = models.CharField(verbose_name='图标', max_length=128)

    def __str__(self):
        return self.title


# 权限表
class Permission(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='标题', max_length=32)
    url = models.CharField(verbose_name='含正则的URL', max_length=128)
    name = models.CharField(verbose_name='URL别名', max_length=64, unique=True, null=True, blank=True)
    menu = models.ForeignKey(verbose_name='所属菜单', to='Menu', null=True, blank=True,
                             help_text='null表示不是菜单;非null表示二级菜单', on_delete=models.CASCADE)
    p_id = models.ForeignKey(verbose_name='关联权限', to='Permission', null=True, blank=True,
                             help_text='对于费菜单权限需要选择一个菜单权限，用户点击非菜单权限时，关联的菜单权限默认展开',
                             related_name='parents', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# 角色表
class Role(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='角色名称', max_length=32)
    permissions = models.ManyToManyField(verbose_name='拥有权限', to='Permission', blank=True)

    def __str__(self):
        return self.title


# 用户表
class UserInfo(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)
    email = models.CharField(verbose_name='邮箱', max_length=64)
    roles = models.ManyToManyField(verbose_name='拥有的角色', to='Role', blank=True)

    def __str__(self):
        return self.name

    '''
    
        引入abstract = True在元类后，此模型将不用于创建任何数据库表。相反，其字段将添加到子类中
    
    '''
    # class Meta:
    #     abstract = True

















