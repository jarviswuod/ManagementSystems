
from django.urls import path

from .views import home, products, loginPage, registerPage, logoutPage, customer

urlpatterns = [
    path('login/', loginPage, name='login'),
    path('register/', registerPage, name='register'),
    path('logout/', logoutPage, name='logout'),


    path('', home, name='home'),
    path('products/', products, name='products'),
    path('customer/', customer, name='customer'),

]
