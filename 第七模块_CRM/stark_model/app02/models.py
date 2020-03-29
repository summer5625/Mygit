from django.db import models

# Create your models here.


# 主机表
class Host(models.Model):

    id = models.AutoField(primary_key=True)
    hostname = models.CharField(verbose_name='主机名', max_length=32)
    ip = models.GenericIPAddressField(verbose_name='IP', protocol='both') # protocol='both'是 协议，支持ipv4和ipv6

    def __str__(self):

        return self.hostname
    

# 角色表
class Role(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='角色名', max_length=32)

    def __str__(self):

        return self.title
