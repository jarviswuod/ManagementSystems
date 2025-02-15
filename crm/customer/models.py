from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=255, null=True,)
    phone = models.PhoneNumberField(null=True)
    email = models.EmailField(max_length=254)
    profile_pic = models.ImageField(null=True)
    user = models.OneToOneField(User, null=True)
