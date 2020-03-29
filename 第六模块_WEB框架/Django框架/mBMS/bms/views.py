from django.shortcuts import render, HttpResponse, redirect
import json
from django.core import serializers


from bms.models import *


def test(request):

    a = Books.objects.filter(id=9)
    print(a)
    return HttpResponse('OK')


def show(request):
    books = []
    book_list = Books.objects.all()
    for item in book_list:
        dist = {}
        author = ''
        bk = Books.objects.filter(id=item.id).first()
        publish = bk.publishb.pname
        authors = bk.authors.all()
        for i in authors:
            author += (i.aname+',')
        dist['id'] = item.id
        dist['title'] = item.title
        dist['price'] = item.price
        dist['pub_date'] = item.pub_date
        dist['publish'] = publish
        dist['author'] = author[:-1]

        books.append(dist)

    return render(request, 'bms/show_book_bases.html', {'books': books,})


def add(request):

    if request.method == 'POST':
        title = request.POST.get('title')
        pub_date = request.POST.get('pub_date')
        price = request.POST.get('price')
        pub = Publish.objects.filter(pname=request.POST.getlist('publish')[0]).first()
        book = Books.objects.create(title=title, pub_date=pub_date, price=price, publishb_id=pub.pid)
        author_l = request.POST.getlist('author')
        for i in author_l:
            aid = i.split(':')[1]
            author = Authors.objects.filter(aid=aid).first()
            book.authors.add(author)

        return redirect('/bms/show')
    else:
        
        publish = Publish.objects.all()
        author = Authors.objects.all()
        
        return render(request, 'bms/add_books.html', {'publish': publish, 'authors': author})


def delete(request, b_id):

    Books.objects.filter(id=b_id).delete()

    return redirect('/bms/show/')


def change(request):

    if request.method == 'POST':

        data = json.loads(request.body)

        b_id = data.get('book_id')
        pub_date = data.get('pub_date')
        price = data.get('price')
        pub = Publish.objects.filter(pname=data.get('pubs')[0]).first()
        Books.objects.filter(id=b_id).update(title=data.get('title'), pub_date=pub_date, price=price, publishb_id=pub.pid)
        author_l = data.get('author')
        book = Books.objects.filter(id=b_id).first()
        book.authors.clear()
        for i in author_l:
            aid = i.split(':')[1]
            author = Authors.objects.filter(aid=aid).first()
            book.authors.add(author)

        return HttpResponse('OK')

    return redirect('/bms/show/')


def book_msg(request):

    book_id = request.GET.get('book_id')

    ret = {}
    a_id = []
    publish = serializers.serialize('json', Publish.objects.all())
    author = serializers.serialize('json', Authors.objects.all())
    book = Books.objects.filter(id=book_id).first()
    pname = book.publishb.pname
    au = book.authors.all()

    for i in au:
        a_id.append(i.aid)

    ret['publish'] = publish
    ret['author'] = author
    ret['a_id'] = a_id
    ret['pname'] = pname
    ret['book'] = serializers.serialize('json', Books.objects.filter(id=book_id))

    return HttpResponse(json.dumps(ret))