from django.db import models


class User(models.Model):

    id = models.AutoField(primary_key=True)
    username = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=16)
    token = models.UUIDField(null=True, blank=True)
    type = models.IntegerField(choices=((1, 'vip'),(2, 'vvip'), (3, '普通')), default=3)
    
    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = '用户表'
        db_table = verbose_name_plural
        