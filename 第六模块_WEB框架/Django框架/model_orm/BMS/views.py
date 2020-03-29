from django.shortcuts import render, HttpResponse, redirect
from orm1.models import Book


def show(request):
    book_list = Book.objects.all()
    
    return render(request, 'BMS/show_books.html', locals())


def add(request):
    
    if request.method == 'GET':
        
        return render(request, 'BMS/add_books.html')
    else:
        title = request.POST.get('title')
        pub_date = request.POST.get('pub_date')
        price = request.POST.get('price')
        publish = request.POST.get('publish')
        ret = Book.objects.create(title=title, pub_date=pub_date, price=price, publish=publish)

        return redirect('/BMS/show/')


def change(request, id):
    book = Book.objects.filter(id=id).first()
    if request.method == 'POST':

        title = request.POST.get('title')
        price = request.POST.get('price')
        date = request.POST.get('pub_date')
        publish = request.POST.get('publish')
        Book.objects.filter(id=id).update(title=title, price=price, pub_date=date, publish=publish)
        return redirect('/BMS/show/')

    return render(request, 'BMS/chang_books.html', {'book': book})


def delete(request, id):
    book = Book.objects.filter(id=id).delete()

    return redirect('/BMS/show/')
