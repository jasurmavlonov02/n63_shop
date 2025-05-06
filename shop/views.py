from django.shortcuts import render
from .models import Product
from django.http.response import HttpResponse

# Create your views here.


def index(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'shop/home.html',context)


def product_detail(request,product_id):
    try:
        product = Product.objects.get(id = product_id)
        context = {'product':product}
        return render(request,'shop/detail.html',context)
    
    except Product.DoesNotExist:
        return HttpResponse('Product Not Found')
    
    
    
    
    