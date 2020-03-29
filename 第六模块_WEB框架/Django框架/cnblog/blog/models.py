from django.db import models
from django.contrib.auth.models import AbstractUser


# 要使用用户认证组件，要用到django_user表，扩展字段时要继承AbstractUser，django_user表也是由AbstractUser来的
class UserInfo(AbstractUser):
    '''
    用户信息表
    '''
    nid = models.AutoField(primary_key=True)
    telephone = models.CharField(max_length=11, null=True, unique=True)
    avatar = models.FileField(upload_to='avatars/', default='avatars/default.png')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    # 与blog表是一对一关系
    blog = models.OneToOneField(to='Blog', to_field='bid', null=True, on_delete=models.CASCADE)

    def __str__(self):

        return self.username


class Blog(models.Model):
    '''
    博客信息表（个人站点）
    与用户表一对一
    '''

    bid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='个人博客标题', max_length=64)
    site_name = models.CharField(verbose_name='站点名称', max_length=64)
    them = models.CharField(verbose_name='博客主题', max_length=32)

    def __str__(self):

        return self.title


class Category(models.Model):
    '''
    博客文章分类表
    '''

    cid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='分类标题', max_length=32)

    # 与博客表一对多，与用户表一对多
    blog = models.ForeignKey(verbose_name='所属博客', to='Blog', to_field='bid', on_delete=models.CASCADE)

    def __str__(self):

        return self.title


class Tag(models.Model):
    '''
    博客文章标签表，与文章表多对多，与用户表一对多
    '''

    tid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='标签名称', max_length=32)
    # 与文章表多对多，与用户表一对多
    blog = models.ForeignKey(verbose_name='所属博客', to='Blog', to_field='bid', on_delete=models.CASCADE)

    def __str__(self):

        return self.title


class Article(models.Model):
    '''
    文章表
    '''

    aid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='文章标题', max_length=64)
    desc = models.CharField(verbose_name='文章描述', max_length=255)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    content = models.TextField()

    comment_count = models.IntegerField(default=0) # 评论数量
    up_count = models.IntegerField(default=0) # 点赞数量
    down_count = models.IntegerField(default=0)

    # 与用户表关联，一对多关系
    user = models.ForeignKey(verbose_name='作者', to='UserInfo', to_field='nid', on_delete=models.CASCADE)
    # 与文章分类表关联，一对多关系
    category = models.ForeignKey(verbose_name='分类', to='Category', to_field='cid', on_delete=models.CASCADE, null=True)
    # 与标签表关联，多对多关系，这里手动创建多对多关系表的中间表
    tags = models.ManyToManyField(to='Tag', through='Article2Tag', through_fields=('article', 'tag'),)

    def __str__(self):

        return self.title


class Article2Tag(models.Model):
    '''
    文章表和标签表的中间表
    '''
    atid = models.AutoField(primary_key=True)
    article = models.ForeignKey(verbose_name='文章', to='Article', to_field='aid', on_delete=models.CASCADE)
    tag = models.ForeignKey(verbose_name='标签', to='Tag', to_field='tid', on_delete=models.CASCADE)

    class Meta:
        '''
        联合唯一
        '''

        unique_together = [('article', 'tag'),]

    def __str__(self):

        v = self.article.title + '---' + self.tag.title

        return v


class ArticleUpDown(models.Model):
    '''
    点赞表
    '''

    udid = models.AutoField(primary_key=True)
    # 与用户表一对多
    user = models.ForeignKey('UserInfo', null=True, on_delete=models.CASCADE)
    # 与文章表一对多
    article = models.ForeignKey('Article', null=True, on_delete=models.CASCADE)
    is_up = models.BooleanField(default=True)

    class Meta:
        # 用户和文章联合唯一
        unique_together = [('article', 'user')]


class Comment(models.Model):
    '''
    评论表
    '''
    cmid = models.AutoField(primary_key=True)
    user = models.ForeignKey(verbose_name='评论者', to='UserInfo', to_field='nid', on_delete=models.CASCADE)
    article = models.ForeignKey(verbose_name='文章', to='Article', to_field='aid', on_delete=models.CASCADE)
    create_time = models.DateTimeField(verbose_name='评论时间', auto_now_add=True)
    content = models.CharField(verbose_name='评论内容', max_length=255)

    parent_comment = models.ForeignKey('self', null=True, on_delete=models.CASCADE)

    def __str__(self):

        return self.content

    