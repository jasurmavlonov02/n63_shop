from django.shortcuts import render,redirect
from .models import Product,Category
from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from .forms import OrderForm,ProductForm,CommentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.db.models.functions import Round
from .utils import product_rating_filter




# Create your views here.


def index(request,category_id=None):
    search_query = request.GET.get('q','')
    filter_type = request.GET.get('filter','')
    categories = Category.objects.all()
    
    
    
    
    if category_id:
        products = Product.objects.filter(category = category_id)
    else:
        products = Product.objects.all() #.order_by('-price')
        
    
        
    if search_query:
        products = products.filter(name__icontains = search_query)
        
    products = products.annotate(avg_rating = Round(Avg('comments__rating'),precision = 2) )

    products = product_rating_filter(filter_type,products)
   
    
    # DRY => Dont Repeat Yourself
    
        
    
    
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'shop/home.html',context)


def product_detail(request,product_id):
    try:
        product = Product.objects.get(id = product_id)
        related_products = Product.objects.filter(category = product.category).exclude(id=product.id)
        context = {
            'product':product,
            'related_products':related_products,
            }
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
            if product.amount < order.quantity or order.quantity == 0:
                # send message
                messages.add_message(
                    request,
                    messages.ERROR,
                    'Don\'t have enough product quantity'
                )
              
               
            else:
                product.amount -= order.quantity
                product.save()
                order.save()
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    'Item successfully ordered'
                )
                return redirect('shop:product_detail',pk)
    context = {
        'form':form,
        'product':product
    }
            
    return render(request,'shop/detail.html',context = context)
            
            
@login_required
def create_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shop:index')
    
    context = {
        'form':form
    }
    return render(request,'shop/product/create.html',context)


@login_required
def edit_product(request):
    pass


@login_required
def delete_product(request,pk):
    product = get_object_or_404(Product,pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('shop:index')
    return render(request,'shop/product/delete.html',{'product':product})




def comment_create(request,pk):
    product =  get_object_or_404(Product,pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        comment = form.save(commit=False)
        comment.product = product
        comment.save()
        return redirect('shop:product_detail',pk)
    
    return render(request,'shop/detail.html',{'form':form})