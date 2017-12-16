from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request,product_id):
    return HttpResponse("You're looking at product %s." % product_id)
