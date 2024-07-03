from django.shortcuts import render

from django.http import JsonResponse

# Create your views here.


def HomePage(request):
    return JsonResponse({"Message": "Hey there"})
