from django.shortcuts import render, HttpResponse
from django.db.models import Avg, Max, Min, Count  #导入聚合函数
from django.db.models import F, Q  #导入F和Q查询


from app01.models import *


def add(request):

    #方法一 向一对多表中添加数据，关联字段orm会将其转化为对应出版社的modles对象
    # book1 = Books.objects.create(title='水浒传', price=20, pub_date='2012-08-03', publishb_id=3)
    # book2 = Books.objects.create(title='三国演义', price=50, pub_date='2011-08-03', publishb_id=2)
    # book3 = Books.objects.create(title='资治通鉴', price=55, pub_date='2016-08-20', publishb_id=1)

    #一对多添加记录
    #方法二 向一对多表中添加数据
    # book_obj = Publish.objects.filter(pid=2).first()

    #这次关联字段添加的是一个出版社的modle对象,从对象中可以取出对应出版社所有信息
    # book = Books.objects.create(title='红楼梦', price=30, pub_date='2011-10-10', publishb=book_obj)
    # print(book.publishb)

    #一对多查询语法
    # book = Books.objects.filter(id=1).first()
    # pb = book.publishb  #得到的是一个对象
    #
    # print(pb.email)

    #多对多添加记录
    # book = Books.objects.filter(id=1).first()
    # book2 = Books.objects.filter(id=2).first()

    # au1 = Authors.objects.filter(aid=5).first()
    # au2 = Authors.objects.filter(aid=3).first()

    #绑定多对多关系API
    # book.authors.add(au1, au2)
    # book.authors.add(1)
    # book2.authors.add(2)

    #解除多对多关系
    # book.authors.remove(au1)
    # book.authors.remove(5)

    #清空多对多关系
    # book.authors.clear()

    #多对多查询语法
    # bb = book2.authors.all() #得到的是一个queryset对象
    # print(bb)



    return HttpResponse('OK')


def base_obj(request):
    '''
    子查询，基于对象的跨表查询：一个表的查询结果作为下一个表查询的条件
    :param request:
    :return:

    '''

    #一对多正向查询：查询西游记这本书出版社的名称
    # book = Books.objects.filter(title='西游记').first()
    # print(book.publishb)
    # print(book.publishb.pname)

    #一对多反向查询：查询化学工业出版社出版的书
    # publish = Publish.objects.filter(pname='化学工业出版社').first()
    # ret = publish.books_set.all()
    # print(ret)

    #多对多的正向查询：查询潜虚的作者
    # book_obj = Books.objects.filter(title='资治通鉴').first()
    # authors = book_obj.authors.all()
    # print(authors)
    # for author in authors:
    #     print(author)


    #多对多反向查询：查询曹雪芹写的书名称
    # au = Authors.objects.filter(aname='曹雪芹').first()
    # book_list = au.books_set.all()
    # print(book_list)
    # for book in book_list:
    #     print(book)


    #一对一表关系查询
    #正向查询：找到吴承恩的联系方式
    # wu = Authors.objects.filter(aname='吴承恩').first()
    # conn = wu.authordetail.telephone
    # print(conn)

    #反向查询：找到地址是山西的作者
    # aut = AuthorDetail.objects.filter(address='山西')
    # for a in aut:
    #     print(a.authors.aname)
    #
    return HttpResponse('OK')


def join(request):
    '''
    双下划线查询，相当于sql中的连表查询
    :param request:
    :return:
    '''
    #一对多正向查询：找出资治通鉴的出版社,join表在values中进行，正向按照如下格式：关联的字段__被查询的字段
    # ret = Books.objects.filter(title='资治通鉴').values('publishb__pname')
    # print(ret)

    #一对多，反向查询：找出资治通鉴的出版社,join表在filter中进行,反向查询按表名：关联表名小写__查询条件字段=查询条件
    # ret = Publish.objects.filter(books__title='资治通鉴').values('pname')
    # print(ret)


    #多对多查询
    #正向查询：查询资治通鉴作者名字,join表在values中进行，正向按照如下格式：关联的字段__被查询的字段
    # ret = Books.objects.filter(title='资治通鉴').values('authors__aname')
    # print(ret)

    #反向查询：查询资治通鉴作者名字,join表在filter中进行,反向查询按表名：关联表名小写__查询条件字段=查询条件
    # ret = Authors.objects.filter(books__title='资治通鉴').values('aname')
    #     # print(ret)


    #一对一表查询
    #正向查询：查询司马光的手机号，join表在values中进行，正向按照如下格式：关联的字段__被查询的字段
    # ret = Authors.objects.filter(aname='司马光').values('authordetail__telephone')
    # print(ret)

    #反向查询：查询司马光的手机号，join表在filter中进行,反向查询按表名：关联表名小写__查询条件字段=查询条件
    # ret = AuthorDetail.objects.filter(authors__aname='司马光').values('telephone')
    # print(ret)

    #连续跨表
    #查询手机号以138开头的作者出版的书籍名称和对应出版社名称
    # ret = Books.objects.filter(authors__authordetail__telephone__startswith='138').values('title', 'publishb__pname')
    # print(ret)

    # 查询手机号以138开头的作者出版的书籍名称和对应出版社名称
    ret = Authors.objects.filter(authordetail__telephone__startswith='138').values('books__title',
                                                                          'books__publishb__pname')
    print(ret)

    return HttpResponse('OK')


#分组查询
def group(request):


    # 聚合查询
    # ret = Books.objects.all().aggregate(avg = Avg('price'), max = Max('price'), min = Min('price'))
    # print(ret)

    #单表下的分组查询values('publishb')分组字段，单表查询中安装主键分组无意义
    # ret = Books.objects.values('publishb').annotate(av = Avg('price'))
    # print(ret)

    #按照主键分组示例：
    # Books.objects.all().annotate()


    #多表查询
    #查询每个出版社出版书籍个数
    # ret = Publish.objects.values('pname').annotate(c = Count('books__id'))
    # print(ret)

    #查询每个作者出版过书籍的最高价格
    # ret = Authors.objects.values('aid').annotate(ma = Max('books__price')).values('aname', 'ma')
    # print(ret)

    #查询每本书籍的名称以及对应的作者
    # ret = Books.objects.values('id').annotate(c = Count('authors__aid')).values('title', 'c')
    # print(ret)

    #查询手机号以138开头的作者，作品的个数
    # ret = AuthorDetail.objects.filter(telephone__startswith='138').values('adid').annotate(c=Count('authors__books__id')).values('authors__aname', 'c')
    # print(ret)

    # 统计书籍作者个数大于1的书籍
    # ret = Books.objects.values('id').annotate(c = Count('authors__aid')).filter(c__gt=1).values('title', 'c')
    # print(ret)


    #F查询
    #查询书籍id大于所在出版社id的书籍
    # ret = Books.objects.filter(id__gt=F('publishb'))
    # print(ret)

    #将每本书价格抬高2元
    # Books.objects.all().update(price = F('price')+2)


    #Q查询
    #查询作者是曹雪芹或者司马光的书籍名称
    # ret = Books.objects.filter(Q(authors__aname='曹雪芹')|Q(authors__aname='司马光'))
    # print(ret)

    #查询书的作者是曹雪芹，并且不是2016年出版的书籍名称
    # ret = Books.objects.filter(Q(authors__aname='曹雪芹') & ~Q(pub_date__year=2016))
    # print(ret)

    #查询在2012年出版，并且价格高于30元的书
    ret = Books.objects.filter(Q(pub_date__year=2016), price__gt=30)
    print(ret)

    return HttpResponse('OK')

'''
子查询，基于对象的跨表查询
一对多查询要点：

    A-B关联表
    关联字段在A表中
    
    正向查询：A---->B，正向查询按字段查询
    反向查询：B---->A，反向查询按照表名查询：关联字段表名称小写__set，得到是queryset对象
    
                                book.publishb
    Book(关联属性：publishb)------------------------->Publish表
                           <------------------------- 
                            aut
                        
多对多查询要点:
    和一对多相似
    
    A-B关联表
    关联字段在A表中
    
    正向查询：A---->B，正向查询按字段查询，得到是queryset对象
    反向查询：B---->A，反向查询按照表名查询：关联字段表名称小写__set，得到是queryset对象
    
    
                             book_obj.authors.all()
    Book(关联属性：publishb)------------------------->Authors表
                           <------------------------- 
                            au.books_set.all()
    
一对一查询要点：
    正向查询按字段 
    反向查询按表名   
    
    
                              wu.authordetail.telephone
    Authors(关联属性：publishb)------------------------->Authors表
                             <------------------------- 
                                au.authors.aname
                                
                                
基于双下划线的多表查询（join）

    正向查询按字段，

'''


def practice(request):

    return HttpResponse('OK')