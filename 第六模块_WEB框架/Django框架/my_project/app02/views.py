from django.shortcuts import render, HttpResponse
from django.urls import reverse

# Create your views here.


def index(request):

    return HttpResponse(reverse('app02:index'))


# def index(request):
#     
#     return HttpResponse('app02:%s'%reverse('app02:index'))
