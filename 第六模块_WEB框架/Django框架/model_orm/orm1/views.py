from django.shortcuts import render, HttpResponse

from orm1.models import Book


def index(request):
    #向表里面插入记录

    #方式一
    # book_obj = Book(id=1, title='红楼梦', state=True, pub_date='2012-05-16', price=50, publish='化学工业出版社')
    # book_obj.save() #在插入记录时必须要保存一下，要不然记录插入不成功

    #方式二（常用）
    # book_obj = Book.objects.create(title='水浒传', state=True, pub_date='2015-05-20', price=60, publish='科学技术出版社')

    #查询
    #1、all()查询结果是一个对象的列表，在django中是一个QuerySet数据类型，只在django中有这个数据类型，具有列表的一些属性
    # book_list = Book.objects.all()

    #2、frist，last方法查询,调用者：QuerySet对象，返回值：model对象
    # book_frist = book_list.first()
    # book_last = book_list.last()

    #3、filter()过滤方法 返回值：QuerySet对象
    # book_l = Book.objects.filter(publish='化学工业出版社')
    # print(book_l.first().title)

    #4、get方法，此方法在有且只有一个查询结果时才有意义，有多个结果或者没有结果都会报错
    # book2 = Book.objects.get(title='西游记')

    #5、exclude方法，排除选中的项
    # book_e = Book.objects.exclude(title='西游记')

    #6、order_by查询结果排序,reverse()倒序
    # book_od = Book.objects.all().order_by('price', '-id')
    # book_odre = Book.objects.all().order_by('price', '-id').reverse()

    #7、count统计查询结果有多少条，返回值：int类型
    # counts = Book.objects.all().count()

    #8、exists()判断是否有查询的结果
    # book_true = Book.objects.filter(price=50).exists()
    # book_flase = Book.objects.filter(price=23).exists()

    #9、values方法，调用者：QuerySet对象，返回值：QuerySet对象，对象里面存放的是一个个的字典
    # book_v = Book.objects.all().values('title', 'price')
    # bb = book_v[0].get('title')
    # print(bb)

    #10、values_list方法,用者：QuerySet对象，返回值：QuerySet对象,里面是一个个的元组，元组里面存放的是查找出来的值
    # book_v_l = Book.objects.all().values_list('title', 'price')

    #11、distinct()方法，去重
    # book_p_d = Book.objects.all().values('price').distinct()

    return render(request, 'orm1/1、vue起步.html', locals())


#模糊查询
def dim_search(request):
    #大于：__gt，小于__lt
    book_big = Book.objects.filter(price__gt=50)
    book_b_s = Book.objects.filter(price__gt=50,price__lt=65)
    print(book_big)
    print(book_b_s)

    #__startswith以什么为开始
    book_start = Book.objects.filter(title__startswith='西')
    print(book_start)

    #__contains包含哪个字段
    book_con = Book.objects.filter(title__contains='记')
    print(book_con)

    #__range在哪个范围
    book_range = Book.objects.filter(price__range=[50, 60])
    print(book_range)

    #__in是不是在这几个值中
    book_in = Book.objects.filter(price__in=[40, 50, 60])
    print(book_in)

    #__year,那个年份
    book_year = Book.objects.filter(pub_date__year=2015)
    book_month = Book.objects.filter(pub_date__month=5)
    book_day = Book.objects.filter(pub_date__day=16)
    print(book_year)
    print(book_month)
    print(book_day)

    #删除数据delete()， 调用者：QuerySet对象或者model对象，返回值：返回删除多少行
    # ret = Book.objects.filter(price=30).delete()
    # print(ret)  #(1, {'orm1.Book': 1})

    #修改数据 调用者：QuerySet对象  返回值：更新多少行,一个整型数字 
    # ret = Book.objects.filter(title='水浒传').update(price=50)
    # print(type(ret), ret)

    return render(request, 'orm1/dim_search.html', locals())
    