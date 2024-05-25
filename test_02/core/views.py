from django.shortcuts import render
from django.http import HttpResponse
from core.models import Category,Product,ProductImages

 
def index(request):
    products=Product.objects.filter(product_status="published",featured=True).order_by("-id")
    context={
        "products":products
    }
    return render (request,'core/index01.html',context)

def prd(request):
    products=Product.objects.filter(product_status="published").order_by("-id")
    context={
        "products":products
    }
    return render (request,'core/prd01.html',context)

def cat(request):
    Categories= Category.objects.all()
    context={
        "categories":Categories
    }
    return render (request,'core/cat01.html',context)