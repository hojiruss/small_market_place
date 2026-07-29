from django.contrib import admin
from .models import Product

class ProductsAdmin(admin.ModelAdmin):
    fields = ["name",
              "price",
              "stock_quantity",
              "seller",
              "description"]

admin.site.register(Product, ProductsAdmin)
