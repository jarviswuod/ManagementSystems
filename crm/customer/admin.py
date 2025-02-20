from django.contrib import admin

# Register your models here.
from .models import Customer, Order, Product, Tag


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email']
    search_fields = ['name', 'phone', 'email']
    list_filter = ['name', 'phone', 'email']
    list_per_page = 10


admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Tag)
