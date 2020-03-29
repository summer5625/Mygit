import re, json, os
from threading import Thread

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Avg, Max, Min, Count, F, Q
from django.db.models.functions import TruncMonth  # 导入日期归档函数
from django.db import transaction  # 引入事务模块
from django.core.mail import send_mail  # 引入发送邮件模块
from bs4 import BeautifulSoup


from blog.tools.valid_img import new_valid_img
from blog.MyForm import UserForm
from cnblog import settings
from blog.models import *


def login(request):
    if request.method == 'POST':

        get_name = request.POST.get('user')
        pwd = request.POST.get('pwd')
        valid_code = request.POST.get('valid_code')
        ret = {'user': None, 'msg': None}
        if valid_code.upper() == request.session.get('valid_code_str').upper():

            user = auth.authenticate(username=get_name, password=pwd)

            if user:
                auth.login(request, user)
                ret['user'] = user.username

                return JsonResponse(ret)

            else:
                ret['msg'] = '密码或用户名错误!'

                return JsonResponse(ret)

        else:
            ret['msg'] = '验证码错误!'

        return JsonResponse(ret)

    return render(request, 'login.html')


# 生成随机验证码图片
def get_valid_img(request):
    data = new_valid_img(request)

    return HttpResponse(data)


# 访问首页
def index(request):
    article_list = Article.objects.all()

    return render(request, 'index.html', locals())


# 注册
def register(request):
    if request.method == 'POST':

        user = UserForm(request.POST)
        response = {'user': None, 'msg': None}

        if user.is_valid():

            response['user'] = user.cleaned_data.get('user')
            avatar_obj = request.FILES.get('photo')

            extra = {}
            if avatar_obj:
                extra['avatar'] = avatar_obj

            UserInfo.objects.create_user(
                username=user.cleaned_data.get('user'),
                password=user.cleaned_data.get('pwd'),
                email=user.cleaned_data.get('email'),
                telephone=user.cleaned_data.get('tel'),
                **extra)

        else:

            response['msg'] = user.errors

        return JsonResponse(response)

    form = UserForm()

    return render(request, 'register.html', locals())


# 注销
@login_required
def logout(request):

    auth.logout(request)

    return redirect('/blog/index/')


def home_site(request, username, **kwargs):
    '''
    个人站点视图函数
    :param request:
    :param username:
    :return:
    '''

    # print(username)

    # print(kwargs)
    ret = UserInfo.objects.filter(username=username).first()

    if not ret:
        return render(request, 'not_found.html')

    # 查询当前站点对象
    blog = ret.blog
    # print('blog', blog)

    # 查询当前作者的文章
    # article_list = ret.article_set.all()

    article_list = Article.objects.filter(user=ret)
    # print('article_list', article_list)

    if kwargs:
        condition = kwargs.get('condition')
        param = kwargs.get('param')

        if condition == 'category':

            article_list = Article.objects.filter(user=ret).filter(category__title=param)

        elif condition == 'tag':

            article_list = Article.objects.filter(user=ret).filter(tags__title=param)

        elif re.search('(?P<year>[0-9]{4})/(?P<month>[0-9]{2})$', param):

            year, month = param.split('/')
            article_list = Article.objects.filter(user=ret).filter(create_time__year=year, create_time__month=month)

        else:

            return render(request, 'not_found.html')

    # 查询每一个分类名称以及对应的文章数
    # article_category = Article.objects.annotate(c = Count('category')).values('category__title', 'c')

    # pk代表主键
    # category_list = Category.objects.values('pk').annotate(c = Count('article__title')).values_list('title', 'c')
    # print(article_category)
    # print(arc)

    # 查询当前站点的每一个分类名称以及对应文章数
    # author_catagory_count = Article.objects.filter(user=ret).annotate(c = Count('category')).values_list('category__title', 'c')
    # category_list = Category.objects.filter(blog=blog).values('pk').annotate(c = Count('article__pk')).values_list('title', 'c')
    # print(author_catagory_count)
    # print(auth_cate)

    # 查询当前站点的每一个标签名称以及对应文章数
    # article_tag_count = Article.objects.filter(user=ret).values('tags__title').annotate(c = Count('tags')).values_list('tags__title', 'c')
    # tag_list = Tag.objects.filter(blog=blog).values('pk').annotate(c = Count('article__aid')).values_list('title', 'c')
    # print(article_tag_count)
    # print(art_tag)

    # 查询当前站点的每一年月名称以及对应文章数

    # 查询文章发布时间是不是大于 2019-10-16
    # date = Article.objects.extra(select={'is_recent':'create_time > 2019-10-16'}).values('title', 'is_recent')
    # print(date)

    # 查询每篇文章的发表日期
    # article_date = Article.objects.extra(select={'y_m_date': "date_format(create_time, '%%Y-%%m-%%d')"}).values('title', 'y_m_date')
    # print(article_date)

    # 统计每个月发表的文章数
    # article_date_count = Article.objects.extra({'y_m_date': "date_format(create_time, '%%Y-%%m')"}).values(
    #     'y_m_date').annotate(c=Count('pk')).values('y_m_date', 'c')
    # print(article_date_count)

    # 统计当前用户每月发表的文章数量

    # 方式一
    # article_month_list = Article.objects.filter(user=ret).extra(
    #     {'y_m_date': "date_format(create_time, '%%Y-%%m')"}).values('y_m_date').annotate(c=Count('pk')).values(
    #     'y_m_date', 'c')
    # print(article_month_list)

    # 方式二

    # date_list = Article.objects.filter(user=ret).annotate(month=TruncMonth('create_time')).values('month').annotate(
    #     c=Count('pk')).values_list('month', 'c')
    # print(date_list)

    return render(request, 'home_site.html', locals())


def article_details(request, username, article_id):
    '''
    文章详情视图
    :param request:
    :return:
    '''

    article_obj = Article.objects.filter(aid=article_id).first()

    comment_list = Comment.objects.filter(article=article_obj)
    
    author = UserInfo.objects.filter(username=username).first()
    
    blog = author.blog

    return render(request, 'article_details.html',
                  {'username': username, 'article_obj': article_obj, 'comment_list': comment_list, 'blog': blog})


@login_required
def digg(request):
    '''
    文章点赞
    :param request:
    :return:
    '''

    response = {'is_handled': True, 'is_up': None}
    user = request.user
    handled = ArticleUpDown.objects.filter(user=user, article__aid=request.POST.get('article_id')).first()

    if ArticleUpDown.objects.filter(user=user, article__aid=request.POST.get('article_id')).exists():

        response['is_handled'] = False
        response['is_up'] = handled.is_up

    else:

        if request.POST.get('is_up') == 'true':

            with transaction.atomic():
                ArticleUpDown.objects.create(user=user, article_id=request.POST.get('article_id'), is_up=True)
                Article.objects.filter(aid=request.POST.get('article_id')).update(up_count=F('up_count') + 1)

        else:

            with transaction.atomic():
                ArticleUpDown.objects.create(user=user, article_id=request.POST.get('article_id'), is_up=False)
                Article.objects.filter(aid=request.POST.get('article_id')).update(up_down=F('up_down') + 1)

    return JsonResponse(response)


@login_required
def comments(request):
    '''
    文章评论视图函数
    :param request:
    :return:
    '''

    response = {}

    user_id = request.user.pk
    comment_content = request.POST.get('comment_content')
    pid = request.POST.get('parent_comment')
    article_id = request.POST.get('article_id')

    # 给插入评论和修改文章评论数目绑定事务
    with transaction.atomic():
        comment_obj = Comment.objects.create(user_id=user_id, article_id=article_id, content=comment_content, parent_comment_id=pid)
        Article.objects.filter(pk=article_id).update(comment_count=F('comment_count')+1)
    
    response['content'] = comment_content
    response['create_time'] = comment_obj.create_time.strftime('%Y-%m-%d %X')
    response['create_user'] = request.user.username

    # 评论成功发送邮件
    article_obj = Article.objects.filter(pk=article_id).first()

    # 这样发送的话 由于网络延时，用户提交评论后邮箱发送成功后评论能容才能显示在用户界面，速度较慢，这里使用多线程来解决这问题
    # send_mail(
    #     '您的文章《%s》新增了一条评论内容'%article_obj.title,  # 邮件主题
    #     comment_content,  # 邮件内容
    #     settings.EMAIL_HOST_USER,  # 发送邮件邮箱
    #     ['458684403@qq.com', ],  # 接收邮件邮箱
    # )

    # 重新开启一个线程来专门发送邮件
    send_email = Thread(target=send_mail, args=(
        '您的文章《%s》新增了一条评论内容'%article_obj.title,  # 邮件主题
        comment_content,  # 邮件内容
        settings.EMAIL_HOST_USER,  # 发送邮件邮箱
        ['1510386346@qq.com', '2804216088@qq.com', '1972657716@qq.com', '573951307@qq.com'],  # 接收邮件邮箱
    ))

    send_email.start()

    return JsonResponse(response)


def get_comment_tree(request):
    
    article_pk = request.GET.get('article_pk')

    tree_list = list(Comment.objects.filter(article=article_pk).order_by('pk').values('content', 'pk', 'parent_comment_id'))
    
    return JsonResponse(tree_list, safe=False)


@login_required
def backend(request):
    '''
    后台管理页面视图
    :param request: 
    :return: 
    '''

    author = request.user
    articles_list = Article.objects.filter(user=author)
    
    return render(request, 'backend/backend.html', locals())


@login_required
def add_article(request):
    '''
    添加文章视图
    :param request:
    :return:
    '''
    
    if request.method == 'POST':
        content = request.POST.get('content')
        title = request.POST.get('title')
        category = request.POST.get('category')
        tag = request.POST.getlist('tag')

        # 将标签过滤掉，只保留标签内的值
        soup = BeautifulSoup(content, 'html.parser')
        desc = soup.text[0:150]

        # 过滤非法标签
        for element in soup.find_all():  # soup.find_all()找出文本中的所有标签元素

            # print(tag.name)
            if element.name == 'script':
                element.decompose()
        with transaction.atomic():

            article = Article.objects.create(title=title, content=str(soup), desc=desc, category_id=category,
                                             user=request.user)
            if tag:
                for i in tag:

                    new_tag = Tag.objects.filter(tid=i).first()
                    Article2Tag.objects.create(article=article, tag=new_tag)

        return redirect('/blog/backend/')

    author = request.user.username
    blog = UserInfo.objects.filter(username=author).first().blog
    category_list = Category.objects.filter(blog=blog)
    tag_list = Tag.objects.filter(blog=blog)
    
    return render(request, 'backend/addarticle.html', locals())


@login_required
def upload(request):

    img = request.FILES.get('upload_img')

    path = os.path.join(settings.MEDIA_ROOT, 'add_article_img', img.name)

    # 将用户在编辑文件时上传的文件保存到上传文件夹中
    with open(path, 'wb') as f:

        for lin in img:
            f.write(lin)

    # 上传文件后在编辑框预览上传的图片
    response = {
        'error': 0,
        'url': 'media/add_article_img/%s'% img.name
    }

    return HttpResponse(json.dumps(response))


@login_required
def delete_article(request, username, article_id):
    '''
    删除文章视图
    :param request:
    :param username:
    :param article_id:
    :return:
    '''

    tags = Article2Tag.objects.filter(article_id=article_id)

    with transaction.atomic():
        if tags:
            tags.delete()

        Article.objects.filter(aid=article_id).delete()

    return redirect('/blog/backend/')


@login_required
def change_article(request, username, article_id):
    '''
    修改文章视图
    :param request:
    :param username:
    :param article_id:
    :return:
    '''

    article = Article.objects.filter(aid=article_id).first()
    tags = Article2Tag.objects.filter(article=article)
    
    if request.method == 'POST':

        content = request.POST.get('content')
        title = request.POST.get('title')
        category = request.POST.get('category')
        tag = request.POST.getlist('tag')

        # 将标签过滤掉，只保留标签内的值
        soup = BeautifulSoup(content, 'html.parser')
        desc = soup.text[0:150]

        for element in soup.find_all():  # soup.find_all()找出文本中的所有标签元素

            if element.name == 'script':
                element.decompose()

        with transaction.atomic():

            if tags:
                article.tags.clear()

            Article.objects.filter(aid=article_id).update(title=title, content=str(soup), desc=desc,
                                                          category_id=category,
                                                          user=request.user)
            for i in tag:
                new_tag = Tag.objects.filter(tid=i).first()
                article.tags.add(new_tag)

        return redirect('/blog/backend/')

    else:
        author = request.user.username
        blog = UserInfo.objects.filter(username=author).first().blog
        category_list = Category.objects.filter(blog=blog)
        tag_list = Tag.objects.filter(blog=blog)
        article_tag_list = []
        article_category = article.category.cid

        for i in tags:
            article_tag_list.append(i.tag.tid)

        send_dict = {
            'article': article,
            'category_list': category_list,
            'tag_list': tag_list,
            'article_tag_list': article_tag_list,
            'article_category': article_category
        }

    return render(request, 'backend/change_article.html', send_dict)











