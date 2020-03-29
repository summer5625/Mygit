from django.db import models


class Books(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8, decimal_places=2)