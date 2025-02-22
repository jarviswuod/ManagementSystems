from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Order, Product, Tag, Customer

from .decorators import authenticated_user

# Create your views here.


@authenticated_user
def loginPage(request):

    if (request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")

    return render(request, "login.html")


@authenticated_user
def registerPage(request):
    form = CreateUserForm()
    if (request.method == "POST"):
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    context = {"form": form}
    return render(request, "register.html", context)


def logoutPage(request):
    logout(request)
    return redirect("login")


@login_required(login_url='login')
def home(request):
    orders = Order.objects.all()
    form = {"orders": orders}
    return render(request, "home.html", form)


@login_required(login_url='login')
def products(request):
    return HttpResponse("This is products")


@login_required(login_url='login')
def customer(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    orders = customer.orders.all()
    print(orders)

    form = {"orders": orders}
    return render(request, "customer.html", form)
