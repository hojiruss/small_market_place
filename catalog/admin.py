from django.contrib import admin
from .models import Product,Profile

class ProductsAdmin(admin.ModelAdmin):
    fields = ["name",
              "price",
              "stock_quantity",
              "seller",
              "description"]

admin.site.register(Product, ProductsAdmin)
admin.site.register(Profile)
