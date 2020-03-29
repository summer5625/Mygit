from django.db import models

# Create your models here.

__all__ = ["Book", "Publisher", "Author"]


class Book(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='图书名称', max_length=32)
    CHOICES = ((1 ,'python'), (2, 'Go'), (3, 'Linux'))
    category = models.IntegerField(choices=CHOICES, verbose_name='图书类别')
    pub_time = models.DateField(verbose_name='出版日期')
    publisher = models.ForeignKey(verbose_name='出版社', to='Publisher', on_delete=None)
    author = models.ManyToManyField(verbose_name='作者', to='Author')

    def __str__(self):

        return self.title

    class Meta:
        verbose_name_plural = '图书表'
        db_table = verbose_name_plural


class Publisher(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='出版社名称', max_length=64)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '出版社表'
        db_table = verbose_name_plural


class Author(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='作者', max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '作者表'
        db_table = verbose_name_plural