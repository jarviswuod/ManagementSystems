from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = PhoneNumberField(null=True, blank=True)
    email = models.EmailField(max_length=254, unique=True)
    profile_pic = models.ImageField(null=True, blank=True)
    user = models.OneToOneField(User, null=True, blank=True,
                                on_delete=models.CASCADE, related_name='customer_profile')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ("DELIVERED", "Delivered"),
        ("PENDING", "Pending"),
        ("OUT OF STOCK", "Out of Stock")
    )
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    status = models.CharField(
        max_length=255, choices=STATUS, default="PENDING")
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Order {self.id} - {self.status}"
