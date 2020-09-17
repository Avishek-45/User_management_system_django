from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.forms import inlineformset_factory
from .forms import Orderform, CreateUserForm
from .filters import OrderFilter
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,allowed_users,admin_only
from django.contrib.auth.models import Group
# Create your views here.


@login_required(login_url='login')
@admin_only
def home(request):
    order = Order.objects.all()
    Customers = customer.objects.all()

    total_customers = Customers.count()
    total_orders = order.count()
    deliverd = order.filter(Status='Delivered').count()
    pending = order.filter(Status='Pending').count()

    content = {'customers': Customers,
               'orders': order,
               'tot_cust': total_customers,
               'tot_orders': total_orders,
               'delivered': deliverd,
               'pending': pending
               }

    return render(request, 'system/Dashboard.html', content)


@login_required(login_url='login')
def customers(request, pk_test):
    Customers = customer.objects.get(id=pk_test)
    # inherting childs objects(order) from parent class i.e customer
    orders = Customers.order_set.all()  # customer ko help bata order call gareko
    total_order = orders.count()
    fil = OrderFilter(request.GET, queryset=orders)
    orders = fil.qs
    context = {'customer': Customers,
               'order': orders, 'total_order': total_order, 'fill': fil}

    return render(request, 'system/customer.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):

    Products = product.objects.all()
    content = {'products': Products}
    return render(request, 'system/products.html', content)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createorder(request, pk):
    # customers=customer.objects.get(id=pk)
    # form=Orderform(initial={'customer':customers})
    OrderFormSet = inlineformset_factory(
        customer, Order, fields=('Products', 'Status'), extra=6)
    Customer = customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=Customer)
    if request.method == "POST":
        formset = OrderFormSet(request.POST, instance=Customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'form': formset}
    return render(request, 'system/order_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateorder(request, pk):

    order = Order.objects.get(id=pk)
    form = Orderform(instance=order)

    if request.method == "POST":
        form = Orderform(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'system/order_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteorder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')

    context = {'item': order}
    return render(request, 'system/delete_order.html', context)


@unauthenticated_user
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        regis = CreateUserForm()  # imported from forms

        if request.method == "POST":
            regis = CreateUserForm(request.POST)
            if regis.is_valid():
                user = regis.save()

                # user register bhayepaxi kun group ma halni bhanna ko lagi-->admin or customer banaune
                group = Group.objects.get(name='customer')
                user.groups.add(group)
                messages.success(request, 'Account was created')
                return redirect('login')

        context = {'regis': regis}
        return render(request, 'system/register.html', context)


@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'system/login.html', context)


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')


def userpage(request):
    return render(request, 'system/userpage.html')
