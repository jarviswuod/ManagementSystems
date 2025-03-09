from django.shortcuts import render
# from django.ht

# Create your views here.


def home(request):
    return render(request, "home.html")
    # return HttpResponse("Home page")


def customer(request):
    return render(request, "customer.html")


def products(request):
    return render(request, "products.html")
