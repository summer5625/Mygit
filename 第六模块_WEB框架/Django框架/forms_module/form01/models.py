from django.db import models


class Userinfo(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)
    email = models.EmailField()
    tel = models.BigIntegerField()

