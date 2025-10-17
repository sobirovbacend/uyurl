from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    cat = Category.objects.all()
    content = {
        "cat":cat
    }

    return render(request,"index.html",content)

# def category(request):
#     cat = Category.objects.all()
#     content = {
#         "cat":cat
#     }
#
#     return render(request,"category.html",content)

def category(request, pk):
    pro = Product.objects.filter(category=pk)
    category = Category.objects.all()
    content = {
        "pro":pro,
        "category":category
    }

    return render(request,"category.html",content)

def product(request):
    pro = Product.objects.all()
    content = {
        "pro":pro
    }

    return render(request,"product.html",content)