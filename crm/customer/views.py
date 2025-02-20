from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
# Create your views here.


def loginPage(request):
    if (request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
    return render(request, "login.html")


def registerPage(request):
    form = CreateUserForm()
    if (request.method == "POST"):
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    context = {"form": form}
    return render(request, "register.html", context)


def home(request):
    return render(request, "home.html")
    # return HttpResponse("This is home")


def products(request):
    return HttpResponse("This is products")
