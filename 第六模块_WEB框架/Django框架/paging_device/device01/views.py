from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator, EmptyPage  #导入分页器, EmptyPage页码出错信息


from device01.models import *


def index(request):

    # book_list = []
    # for i in range(100):
    #     book = Books(title='book_%s' % i, price=i * 2)
    #     book_list.append(book)
    #
    # Books.objects.bulk_create(book_list) # 批量向数据库中插入数据记录

    books = Books.objects.all()

    #分页器

    paginator = Paginator(books, 5) #两个参数，第一个参数是所有的内容列表，第二个参数是每页显示多少条内容
    current_page_num = int(request.GET.get('page', 1))  # 获取当前页面中显示的页码数，其中第二个参数值默认第一页

    print(paginator.count) # 数据总数
    print(paginator.num_pages) #总也页数
    print(paginator.page_range) #页码的列表

    if paginator.num_pages > 11:
        if current_page_num - 5 < 1:
            pag_range = range(1, 12)
        elif current_page_num + 5 > paginator.num_pages:
            pag_range = range(paginator.num_pages - 10, paginator.num_pages + 1)
        else:
            pag_range = range(current_page_num - 5, current_page_num + 6)
    else:
        pag_range = paginator.page_range

    try:
        # current_page_num = int(request.GET.get('page', 1)) #获取当前页面中显示的页码数，其中第二个参数值默认第一页

        current_page = paginator.page(current_page_num)

        # print(current_page.has_next())  #判断当前页面是否还有下一页
        # print(current_page.next_page_number()) #获取当前页面下一页的页码
        # print(current_page.has_previous()) #判断当前页面是否还有上一页
        # print(current_page.previous_page_number()) #获取当前页面的上一页页码

            #显示某一页中的数据
            # print(current_page.object_list) #方式一

            # for i in current_page:  #方式二
            #     print(i)

    except EmptyPage as e: #页码不在范围内时显示第一页内容
        current_page = paginator.page(current_page_num)

    return render(request, 'device01/1、vue起步.html', locals())
