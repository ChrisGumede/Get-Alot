from django.shortcuts import render
from . models import Product
from .models import models
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    product_objects = Product.objects.all().order_by('title') 

    #create search funtionality
    product_name = request.GET.get('product_name')
    if product_name != '' and product_name is not None:
        product_objects = product_objects.filter(title__icontains = product_name)

    #creating pagination intances
    paginator = Paginator(product_objects,5)
    page_number = request.GET.get('page')
    product_objects = paginator.get_page(page_number)
    return render(request,'shop/index.html',{'product_objects':product_objects})

def detail(request,id):
    Product_object = Product.objects.get(id=id)
    return render(request,'shop/detail.html',{'product_object':Product_object})

def ckeckout(request):
    return render(request,'shop/ckeckout.html')


