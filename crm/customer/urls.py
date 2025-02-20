
from django.urls import path

from .views import home, products, loginPage, registerPage

urlpatterns = [
    path('login/', loginPage, name='login'),
    path('register/', registerPage, name='register'),

    path('', home, name='home'),
    path('products/', products, name='products'),

]
