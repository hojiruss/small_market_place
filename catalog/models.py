from django.contrib.auth.models import User
from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    stock_quantity = models.DecimalField(max_digits=1000, decimal_places=2)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


