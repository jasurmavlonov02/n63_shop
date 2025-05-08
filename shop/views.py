from django.shortcuts import render,redirect
from .models import Product,Category
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from .forms import OrderForm


# Create your views here.


def index(request,category_id=None):
    search_query = request.GET.get('q','')
    categories = Category.objects.all()
    
    
    
    
    if category_id:
        products = Product.objects.filter(category = category_id)
    else:
        products = Product.objects.all() #.order_by('-price')
        
    if search_query:
        products = products.filter(name__icontains = search_query)
    
    
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'shop/home.html',context)


def product_detail(request,product_id):
    try:
        product = Product.objects.get(id = product_id)
        context = {'product':product}
        return render(request,'shop/detail.html',context)
    
    except Product.DoesNotExist:
        return HttpResponse('Product Not Found')
    
    
def order_detail(request,pk):
    # product = Product.objects.get(id = pk)
    product = get_object_or_404(Product,pk=pk)
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            return redirect('index')
    context = {
        'form':form,
        'product':product
    }
            
    return render(request,'shop/detail.html',context = context)
            