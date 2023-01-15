from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 'customers': customers, 'total_orders': total_orders, 'delivered': delivered,
               'pending': pending}

    return render(request, 'accounts/dashboard.html', context)


def products(request):
    product = Products.objects.all()

    return render(request, 'accounts/products.html', {'products': product})


def customer(request, pk_test):
    custom = Customer.objects.get(id=pk_test)

    orders = custom.order_set.all()
    order_count = orders.count()

    context = {'customer': custom, 'orders': orders, 'order_count': order_count}
    return render(request, 'accounts/customer.html', context)


def createOrder(request):
    context = {}

    return render(request, 'accounts/order_form.html', context)