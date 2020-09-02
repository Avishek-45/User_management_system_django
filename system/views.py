from django.shortcuts import render,HttpResponse
from .models import *

# Create your views here.

def home(request):
    order=Order.objects.all()
    Customers=customer.objects.all()

    total_customers=Customers.count()
    total_orders=order.count()
    deliverd=order.filter(Status='Delivered').count()
    pending=order.filter(Status='Pending').count()

    content={'customers':Customers,
    'orders':order,
    'tot_cust':total_customers,
    'tot_orders':total_orders,
    'delivered':deliverd,
    'pending':pending
    }

    return render(request,'system/Dashboard.html',content)

def customers(request,pk_test):
    Customers=customer.objects.get(id=pk_test)
    #inherting childs objects(order) from parent class i.e customer
    orders=Customers.order_set.all()
    total_order=orders.count()

    context={'customer':Customers,'order':orders,'total_order':total_order}

    return render(request,'system/customer.html',context)

def products(request):
    Products=product.objects.all()
    content={'products':Products}
    return render(request,'system/products.html',content)