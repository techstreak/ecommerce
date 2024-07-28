from django.contrib import admin
from .models import Client, Token , Product, Order

# Register your models here.

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Client)
admin.site.register(Token)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'image', 'image_url']