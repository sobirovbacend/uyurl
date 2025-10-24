from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import ProductForm, SuppliersForm, CategoryForm


def index(request):
    cat = Category.objects.all()
    pro1 = Product.objects.all()
    content = {
        "cat":cat,
        "pro1":pro1
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


# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = NewsForm()
        
#     return render(request,'add_news.html',{'form':form})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form = ProductForm()
    
    return render(request,'add_product.html', {'form': form})


def add_suppliers(request):
    if request.method =='POST':
        form = SuppliersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')


    else:
        form = SuppliersForm()

    return  render(request,'add_suppliers.html',{'form':form})


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')


    else:
        form = CategoryForm()


    return render(request,'add_category.html' ,{'form':form})


