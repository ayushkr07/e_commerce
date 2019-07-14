from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.
def index(request):
    #products=Product.objects.all()
    #n=len(products)
    #nSlides= n//4 + ceil((n/4)-(n//4))
    #allProd=[[products,range(1,nSlides)],
     #        [products,range(1,nSlides)]]
    #stf={'allProd':allProd}

    allProd = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        products = Product.objects.filter(category=cat)
        n = len(products)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProd.append([products, range(1,nSlides)])
    stf={'allProd':allProd}
    return render(request,'shop/index.html',stf)

def about(request):
    return HttpResponse("We are at about")

def contact(request):
    return HttpResponse("We are at contact")

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def productView(request):
    return HttpResponse("We are at product view")

def checkout(request):
    return HttpResponse("We are at checkout")
