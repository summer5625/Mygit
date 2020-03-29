from django.db import models


#出版社表
class Publish(models.Model):

    pid = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    email = models.EmailField()

    def __str__(self):

        return self.pname


#作者详情表
class AuthorDetail(models.Model):

    adid = models.AutoField(primary_key=True)
    birthday = models.DateField()
    telephone = models.BigIntegerField()
    address = models.CharField(max_length=64)


#作者表
class Authors(models.Model):

    aid = models.AutoField(primary_key=True)
    aname = models.CharField(max_length=32)
    age = models.IntegerField()

    #与AuthorDetail建立一对一关系，在1.0版本的django中在建立关联字段时会默认加上on_delete=models.CASCADE字段，但是在2.0版本
    #中必须手动添加on_delete=models.CASCADE该字段，否则在建立表时会报错
    authordetail = models.OneToOneField(to='AuthorDetail', to_field='adid', on_delete=models.CASCADE)


    def __str__(self):

        return self.aname


# 图书信息表
class Books(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    pub_date = models.DateField()

    #与publish表建立一对多的关系,再建立表关系是被关联表名称最好用引号将表名称括起来，如果直接填表名称的话，那么被关联表，在关联表下方，
    #则会找不到北被关联表
    publishb = models.ForeignKey(to='Publish', to_field='pid', on_delete=models.CASCADE)

    #创建多对多关系，django在创建多对多关系时不需要在自己创建关联表，django会自己自动生成关联表,关联表的名称是关联表的名称_关联字段名称
    authors = models.ManyToManyField(to='Authors')


    def __str__(self):

        return self.title
















