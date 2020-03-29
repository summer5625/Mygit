from django.db import models


class User(models.Model):
    
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)